import numpy as np
import tensorflow as tf
from wavenet import WaveNetModel


class TestGeneration(tf.test.TestCase):

    def setUp(self):
        self.net = WaveNetModel(batch_size=1,
                                dilations=[1, 2, 4, 8, 16, 32, 64, 128, 256],
                                filter_width=2,
                                residual_channels=16,
                                dilation_channels=16,
                                quantization_channels=128,
                                skip_channels=32)

    def testGenerateSimple(self):
        '''does nothing'''
        self.assertAllEqual([128], [128])
        self.assertTrue(True)
        self.checkpoint = "../save/model.ckpt-804"

        saver = tf.train.import_meta_graph(self.checkpoint + '.meta',
                                           clear_devices=False)
        saver.restore(sess, args.checkpoint)

        config = {}
        for cfg_tensor in tf.get_collection("config"):
            config[cfg_tensor.name.split(":")[0]] = sess.run(cfg_tensor)

        if args.fast_generation:
            next_sample = tf.get_collection("predict_proba_incremental")[0]
        else:
            next_sample = tf.get_collection("predict_proba")[0]

        if args.dat_seed:
            raise NotImplementedError("No seed function yet...")
        else:
            data_feed = np.zeros([config['receptive_field_size'], config['data_dim']], dtype=np.float32)
            gc_feed = np.zeros(config['receptive_field_size'], dtype=np.int32)
            lc_feed = np.zeros(config['receptive_field_size'], dtype=np.int32)

        last_sample_timestamp = datetime.now()

        try:
            for step in range(args.samples):
                if args.fast_generation:
                    outputs = [next_sample]
                    outputs.extend(net.push_ops)
                    window_data = data_feed[-1]

                    # See Alex repository for feeding in initial samples...
                else:
                    if len(data_feed) > config['receptive_field_size']:
                        window_data = data_feed[-config['receptive_field_size']:]
                        window_gc = gc_feed[-config['receptive_field_size']:]
                        window_lc = lc_feed[-config['receptive_field_size']:]
                    else:
                        window_data = data_feed[:]
                        window_gc = gc_feed[:]
                        window_lc = lc_feed[:]

                    outputs = [next_sample]
                prediction = sess.run(ouputs, feed_dict={'samples:0': window_})
                data_feed = np.append(data_feedm prediction, axis=0)

                gc_feed = np.append(gc_feed, "Angry")
                lc_feed = np.append(lc_feed, "Eh")
                print("%5i %s %s \n %s" % (step,
                                           colored(CURRENT_EMOTION, 'blue'),
                                           colored(CURRENT_PHONEME, 'white',
                                           'on_grey', attrs=['bold']),
                                           colored(str(prediction), 'grey')))


if __name__ == '__main__':
    tf.test.main()
