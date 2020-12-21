"""Code written to solve objective 11a"""

import random
from mt19937predictor import MT19937Predictor


def nonce_predictor(nonces, blockchain, target_block):
    """Predict the nonce for the target block."""

    # set up the predictor with the nonces as 64-bit integers
    predictor = MT19937Predictor()
    for nonce in nonces[-624:]:
        predictor.setrandbits(nonce, 64)

    # predict blocks until we reach the target block
    block_index = blockchain.index + 1
    for i in range(block_index, target_block):
        print(f'Predicting nonce for block {i}...')
        next_nonce = predictor.getrandbits(64)
    print('The target block will have the nonce:', hex(next_nonce))

