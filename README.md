# MUSE-inspired Adversarial English Embedding Transformation

This repository contains an implementation inspired by Facebook's Multilingual Unsupervised Embeddings (MUSE). Although originally designed for bilingual alignment (e.g., English–Hindi), our implementation focuses on understanding the adversarial training process using only English embeddings. In this setup, the goal is to learn a mapping that transforms English embeddings, with the discriminator distinguishing between the original and the transformed (fake) embeddings.

## Project Overview

The original MUSE approach aligns embedding spaces of two languages without parallel data by employing adversarial training. In our simplified version, we use only English embeddings during the adversarial phase. This allows us to focus on the fundamental ideas behind the training process—how the mapping network learns to fool the discriminator and thereby capture intrinsic properties of the embedding space.

## Methodology

### Adversarial Training with English Embeddings

Unlike traditional bilingual setups, our approach uses solely English embeddings for both components of the adversarial network:

#### Mapping Network (Generator)
- **Objective:** Learn a transformation of English embeddings so that the output (fake embeddings) mimics the statistical properties of the original English embeddings.
- **Mechanism:** The mapping network is optimized to fool the discriminator by producing embeddings that are indistinguishable from the real ones.

#### Discriminator
- **Objective:** Distinguish between original (real) English embeddings and transformed (fake) embeddings.
- **Mechanism:** The discriminator is trained to correctly classify which embeddings are original and which are generated. This feedback, in turn, guides the mapping network to improve its transformation.

## Training Process

### Initialization
- Pre-trained English embeddings are loaded.

### Adversarial Loop
- **Step 1:** A batch of English embeddings is passed through the mapping network, generating "fake" embeddings.
- **Step 2:** Both the original English embeddings (real) and the transformed embeddings (fake) are fed into the discriminator.
- **Step 3:** The discriminator is updated to correctly label the inputs as real or fake.
- **Step 4:** Simultaneously, the mapping network is trained with the objective of fooling the discriminator—making its output appear as real as the original embeddings.
- **Outcome:** Through iterative updates, the mapping network learns a transformation that yields embeddings closely resembling the original distribution.

## Downstream Application

Although the adversarial stage uses only English embeddings, the learned mapping can later be incorporated into a bilingual translation framework (e.g., aligning with Hindi embeddings) through additional processing steps not covered in the adversarial training.
