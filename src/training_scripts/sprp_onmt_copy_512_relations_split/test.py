from src import evaluate
import os

def main():
    model_name = 'sprp_onmt_copy_512_relations_split'

    base_path = '/home/nlp/aharonr6'

    moses_path = base_path + '/git/mosesdecoder'

    test_dirs_path_prefix = base_path + '/git/Split-and-Rephrase/evaluation-directories-RDFs-relations/test/'

    # the file containing the ids of the test sentences
    test_sent_ids_path = base_path + '/git/Split-and-Rephrase/benchmark/complex-sents/test-rdfs-relations.id'

    # a directory that will hold single sentence files for the hypotheses
    test_hypothesis_sents_dir = base_path + '/git/phrasing/models/{}/test_complex_output_sents/'.format(model_name)
    if not os.path.exists(test_hypothesis_sents_dir):
        os.mkdir(test_hypothesis_sents_dir)

    test_target = base_path + '/git/phrasing/models/{}/test.complex.unique.output'.format(model_name)

    print 'starting multi-ref evaluation...'
    evaluate.eval_bleu_min_rouge(moses_path,
                                                                                                    test_sent_ids_path,
                                                                                                    test_hypothesis_sents_dir,
                                                                                                    test_target,
                                                                                                    test_dirs_path_prefix)

    os.system('cat {}'.format(test_target+'.eval'))
    return

if __name__ == '__main__':
    main()