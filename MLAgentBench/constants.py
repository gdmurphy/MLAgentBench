import os

ALL_BASE_RUNTIME = {
        "base-competition" : {
            "dev" : 100,
            "test" : 100,
            },
        "llm-merging" : {
            "dev" : 3447.39514565467,
            "test" : 1811.927922,
            },
        "backdoor-trigger-recovery" : {
            "dev" : 481.1659276,
            "test" : 429.746381,
            "debug" : 400,
            },
        "perception_temporal_action_loc" : {
            "dev" : 1238.63,
            "test" : 361.45,
        },
        # TODO: add the runtime (unit in seconds) of your new tasks here.
        "meta-learning": {
            "val" : 1720.0941224098206,
            "test" : 1783.7426211833954
        }
    }

ALL_BASE_PERFORMANCE = {
        "base-competition" : {
            "dev" : 0.5,
            "test" : 0.5,
            },
        "llm-merging" : {
            # range 0-1
            "dev" : 0.73,
            "test" : 0.49,
            },
        "backdoor-trigger-recovery" : {
            # range 0-100
            "dev" : 8.331147359458377,
            "test" : 12.972998823683664,
            "debug" : 2,
            },
        "perception_temporal_action_loc" : {
            # range 0-1
            "dev" : 0.237,
            "test" : 0.126,
        },
        # TODO: add the baseline performance of your new tasks here.
        "meta-learning" : {
            # range 0-1
            "val" : 0.21006902462067517,
            "test" : 0.15242809189567028
        }
    }



MLR_BENCH_DIR = os.getenv("MLR_BENCH_DIR", "~/MLAgentBench") # absolute path is preferred
