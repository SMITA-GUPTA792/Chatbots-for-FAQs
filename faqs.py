"""
FAQ dataset: Artificial Intelligence.

Each entry is a question/answer pair the chatbot can match against.
Feel free to add, edit, or remove entries — the chatbot rebuilds its
matching index automatically from whatever is in this list.
"""

FAQS = [
    {
        "question": "What is Artificial Intelligence?",
        "answer": "Artificial Intelligence (AI) is the field of computer science focused on building "
                   "systems that can perform tasks that normally require human intelligence, such as "
                   "understanding language, recognizing images, making decisions, and solving problems.",
    },
    {
        "question": "What is the difference between AI, Machine Learning, and Deep Learning?",
        "answer": "AI is the broad goal of making machines act intelligently. Machine Learning (ML) is a "
                   "subset of AI where systems learn patterns from data instead of following explicit rules. "
                   "Deep Learning is a subset of ML that uses multi-layered neural networks to learn from "
                   "large amounts of data.",
    },
    {
        "question": "What are the different types of AI?",
        "answer": "AI is often grouped into Narrow AI (designed for a specific task, like spam filtering), "
                   "General AI (hypothetical AI with human-level reasoning across any task), and "
                   "Superintelligent AI (a theoretical AI surpassing human intelligence in all areas). "
                   "Today, almost all existing AI systems are Narrow AI.",
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a method of teaching computers to learn patterns from data and make "
                   "predictions or decisions without being explicitly programmed for every scenario.",
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning is a machine learning approach where a model is trained on labeled "
                   "data, meaning each training example comes with the correct answer, so the model learns "
                   "to map inputs to outputs.",
    },
    {
        "question": "What is unsupervised learning?",
        "answer": "Unsupervised learning is a machine learning approach where the model is given data without "
                   "labels and must find patterns, groupings, or structure on its own, such as clustering "
                   "similar items together.",
    },
    {
        "question": "What is reinforcement learning?",
        "answer": "Reinforcement learning is a machine learning approach where an agent learns to make "
                   "decisions by taking actions in an environment and receiving rewards or penalties, "
                   "gradually improving its strategy over time.",
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a computing system loosely inspired by the human brain, made up of "
                   "layers of connected nodes (neurons) that process data and learn to recognize patterns "
                   "through training.",
    },
    {
        "question": "What is Natural Language Processing?",
        "answer": "Natural Language Processing (NLP) is a branch of AI that enables computers to understand, "
                   "interpret, and generate human language, used in applications like chatbots, translation, "
                   "and sentiment analysis.",
    },
    {
        "question": "What is computer vision?",
        "answer": "Computer vision is a field of AI that trains computers to interpret and understand visual "
                   "information from images or videos, such as recognizing objects, faces, or text.",
    },
    {
        "question": "Who is considered the father of Artificial Intelligence?",
        "answer": "John McCarthy is widely considered the father of Artificial Intelligence; he coined the "
                   "term 'Artificial Intelligence' in 1956 at the Dartmouth Conference.",
    },
    {
        "question": "What is the Turing Test?",
        "answer": "The Turing Test, proposed by Alan Turing in 1950, evaluates a machine's ability to "
                   "exhibit intelligent behavior indistinguishable from that of a human, typically through "
                   "a text-based conversation.",
    },
    {
        "question": "What is an AI chatbot?",
        "answer": "An AI chatbot is a software application that uses AI techniques, like natural language "
                   "processing, to simulate human-like conversation and answer user questions automatically.",
    },
    {
        "question": "What is a large language model?",
        "answer": "A large language model (LLM) is a type of AI model trained on vast amounts of text data "
                   "to understand and generate human-like language, powering applications like chatbots and "
                   "writing assistants.",
    },
    {
        "question": "What are some real-world applications of AI?",
        "answer": "AI is used in recommendation systems (Netflix, Amazon), voice assistants (Siri, Alexa), "
                   "fraud detection, medical diagnosis, self-driving cars, spam filters, facial recognition, "
                   "and language translation, among many other areas.",
    },
    {
        "question": "Is AI going to replace human jobs?",
        "answer": "AI is likely to automate certain repetitive or data-heavy tasks, which may change or "
                   "eliminate some jobs, but it is also expected to create new roles and augment human "
                   "capabilities rather than replace humans entirely in most fields.",
    },
    {
        "question": "What are the ethical concerns around AI?",
        "answer": "Key ethical concerns include bias in AI decision-making, privacy violations, lack of "
                   "transparency in how decisions are made, job displacement, misuse for surveillance or "
                   "misinformation, and the need for accountability when AI systems cause harm.",
    },
    {
        "question": "What is AI bias?",
        "answer": "AI bias occurs when an AI system produces unfair or skewed results because the data it "
                   "was trained on reflects existing human biases or lacks diversity, leading to "
                   "discriminatory outcomes.",
    },
    {
        "question": "What is the difference between AI and robotics?",
        "answer": "AI is about creating intelligent decision-making systems, while robotics is about "
                   "building physical machines that can interact with the world. Robots often use AI for "
                   "perception and decision-making, but not all robots are AI-powered, and not all AI runs "
                   "on a physical robot.",
    },
    {
        "question": "What is overfitting in machine learning?",
        "answer": "Overfitting happens when a machine learning model learns the training data too closely, "
                   "including its noise and outliers, causing it to perform well on training data but poorly "
                   "on new, unseen data.",
    },
    {
        "question": "What is a dataset used for in AI?",
        "answer": "A dataset is a collection of data used to train, validate, and test an AI model so it can "
                   "learn patterns and be evaluated on how well it generalizes to new examples.",
    },
    {
        "question": "What programming languages are commonly used for AI?",
        "answer": "Python is the most popular language for AI due to its simplicity and rich ecosystem of "
                   "libraries (TensorFlow, PyTorch, scikit-learn). Other languages used include R, Java, "
                   "and C++ for performance-critical applications.",
    },
    {
        "question": "What is the history of Artificial Intelligence?",
        "answer": "AI research began in the 1950s with pioneers like Alan Turing and John McCarthy. It went "
                   "through periods of rapid progress and 'AI winters' of reduced funding, before "
                   "accelerating again in the 2010s thanks to big data, more powerful computing hardware, "
                   "and advances in deep learning.",
    },
    {
        "question": "What is Artificial General Intelligence (AGI)?",
        "answer": "Artificial General Intelligence (AGI) refers to a hypothetical AI system with the ability "
                   "to understand, learn, and apply knowledge across a wide range of tasks at a level "
                   "comparable to or exceeding human intelligence. AGI does not yet exist.",
    },
    {
        "question": "How does AI learn from data?",
        "answer": "AI models learn from data by adjusting internal parameters to minimize the difference "
                   "between their predictions and the correct answers, a process typically driven by "
                   "algorithms like gradient descent during training.",
    },
    {
        "question": "What is the difference between AI and automation?",
        "answer": "Automation follows fixed, pre-programmed rules to perform repetitive tasks, while AI can "
                   "learn from data, adapt, and make decisions in situations it wasn't explicitly "
                   "programmed for.",
    },
    {
        "question": "Can AI be creative?",
        "answer": "Modern generative AI models can produce text, images, music, and code that appear "
                   "creative by learning patterns from large datasets, though whether this counts as true "
                   "creativity (versus sophisticated pattern recombination) is still debated.",
    },
    {
        "question": "What skills do I need to start learning AI?",
        "answer": "A good starting point includes basic programming (especially Python), foundational math "
                   "(linear algebra, statistics, probability), and an understanding of core machine learning "
                   "concepts before moving on to specialized libraries and frameworks.",
    },
    {
        "question": "What is the difference between AI and data science?",
        "answer": "Data science focuses on extracting insights and knowledge from data using statistics, "
                   "analysis, and visualization, while AI focuses on building systems that can perform "
                   "intelligent tasks. The two fields overlap heavily, especially in machine learning.",
    },
    {
        "question": "Is AI dangerous?",
        "answer": "AI itself isn't inherently dangerous, but risks can arise from misuse, poorly designed "
                   "systems, biased data, lack of oversight, or deploying AI in high-stakes situations "
                   "without proper safety testing. Responsible development and regulation aim to reduce "
                   "these risks.",
    },
]
