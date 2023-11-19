# A.I. Logic Puzzle Solver

## Authors

- Eulices Martinez de la cruz
- Aaron Lee
- Nelson Phan
- Abel Mendoza
- James Thuyen

## Problem Statement

In this Logic Puzzle, Simon takes an "adventure holiday" every year with a friend to some new location within the United States. The goal is to develop an inference algorithm that checks possible solutions, formulating each possible solution as a sentence, and applying an inference algorithm to check whether each sentence is entailed by the knowledge base.

## About

### What is a Logic Puzzle?

A logic puzzle is a type of brainteaser or game that requires the solver to use deductive reasoning to arrive at a solution. These puzzles often involve a set of clues or constraints that, when properly interpreted, lead to a unique solution. Logic puzzles come in various forms, including grid-based puzzles, riddles, and complex scenarios that require careful analysis to solve.

In our project, we tackled a specific type of logic puzzle where Simon embarks on an "adventure holiday" each year with a friend to different locations within the United States. The challenge is to deduce the details of each trip, such as the friend, activity, year, and state, based on a set of given clues.

### Methods Used

#### Propositional Logic and Inference Algorithms

To approach this logic puzzle, we utilized propositional logic to represent statements about the relationships between different elements of the puzzle. Each clue was translated into a logical sentence, forming a knowledge base. We then employed inference algorithms to derive additional information from the given clues.

#### Proof by Resolution

Our chosen algorithm for making inferences was "Proof by resolution." This method involves deriving new logical sentences by resolving existing ones, gradually building a more comprehensive understanding of the puzzle. The algorithm aims to determine whether a particular statement is entailed by the knowledge base.

### How to Use the Solver

1. **Input Clues:** Provide the initial clues about the logic puzzle, including information about friends, years, activities, and any given relationships.
2. **Inference Algorithm:** Choose the desired inference algorithm, such as "Proof by resolution."
3. **Generate Solutions:** Run the solver to generate possible solutions based on the input clues and the applied inference algorithm.
4. **Review Results:** Examine the derived logical sentences and solutions to understand the details of Simon's adventure holidays.

Feel free to explore and experiment with different sets of clues and inference algorithms to enhance the solver's capabilities.

## Knowledge Base

In the context of our logic puzzle solver, a Knowledge Base (KB) plays a crucial role in representing and organizing information about the puzzle. A Knowledge Base is a repository of statements, facts, or propositions that the solver uses to derive conclusions and make inferences.

### Role of the Knowledge Base

1. **Information Representation:** The Knowledge Base encapsulates the initial clues provided for the logic puzzle. Each clue is translated into a logical sentence using propositional logic. For example, statements like "Gladys went kayaking" or "Lillie's trip was in 2003" become part of the Knowledge Base.
2. **Inference Support:** The Knowledge Base serves as the foundation for the inference algorithms to operate. These algorithms use the logical sentences in the Knowledge Base to derive new statements or conclusions. This iterative process enhances the depth of understanding about the puzzle and helps unveil hidden relationships between elements.
3. **Consistency Checking:** The Knowledge Base allows the solver to check the consistency of the information. It helps identify contradictions or conflicts within the provided clues and derived statements. Inconsistent information may indicate errors in the input or require further analysis.

### Building the Knowledge Base

1. **Clue Translation:** Each given clue is translated into a propositional logic sentence and added to the Knowledge Base. These sentences collectively form the set of initial assumptions.
2. **Inference Steps:** As the solver applies inference algorithms, new logical sentences are generated based on the existing Knowledge Base. These sentences are subsequently added to the Knowledge Base, enriching it with additional information.
3. **Iterative Process:** The process of adding and updating the Knowledge Base is iterative. The solver refines its understanding of the puzzle by continuously building upon the existing set of logical sentences.

### Example Knowledge Base Entry

Consider the clue "Gladys went kayaking." In the Knowledge Base, this clue is represented using propositional logic: `G ∧ KY` (Gladys and Kayaking). Similarly, each clue is translated and incorporated into the Knowledge Base, forming the basis for the logical reasoning process.

Understanding the role of the Knowledge Base is essential for effectively utilizing the logic puzzle solver and navigating through the intricacies of the given clues.

---

## Categories

### Friends:

- Gladys
- Lillie
- Pam
- Victor

### Years:

- 2001
- 2002
- 2003
- 2004

### Activities:

- Camping
- Hang gliding
- Kayaking
- Skydiving

## Clues

1. The friend that went skydiving took their trip 2 years before the friend who went hang gliding.
2. Gladys either went kayaking or went on vacation in 2004.
3. Lillie went on vacation in 2003.
4. The four trips are: Lillie in 2003, the hang gliding trip, the vacation with Victor, and one with Gladys.

## Inferred Data

Based on the clues, propositional logic sentences were added to the knowledge base. Here are some examples:

- The hang gliding trip did not happen in 2001.
- Gladys went kayaking.
- Pam went on a trip in 2004.

## Algorithm: Proof by Resolution

We implemented the "Proof by resolution" algorithm to make inferences based on the propositional logic sentences in our knowledge base.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](https://chat.openai.com/c/LICENSE.md) file for details.

## Documentation

[https://docs.google.com/document/d/1Rr6eAtqm1vNXV1tBA0NyWEss199xRCpqoyxP63mbjec/edit#heading=h.sf1rjk24v8by](https://docs.google.com/document/d/1Rr6eAtqm1vNXV1tBA0NyWEss199xRCpqoyxP63mbjec/edit#heading=h.sf1rjk24v8by)
===========================================================================================================

## Install the following requirements by running

```
pip install -r requirements.txt
```

## Running program

Open `CPSC482-Project-2-update.ipynb` file. Jupiter Notebook will allow you to run code from code cell. All other code in the cpsc481project2 folder are for fun

>>>>>>> a2d3aacadccc4e746a2aaef9bad9e38ec953f083
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>
