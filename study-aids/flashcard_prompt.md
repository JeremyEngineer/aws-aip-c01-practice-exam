# Flash Card Generation Prompt

I'm studying for my "AWS Certified Generative AI Developer – Professional (AIP-C01 – English)" exam. Please make me some flash cards. Please make them based on my flash cards and focus on content that would likely be on the exam.

Here are some sample exam questions from the practice exam (full set of 20 questions with answer options, explanations, and correct answers is in the accompanying file `AIP-C01_practice_questions.md`):

---

> Paste or reference the contents of `AIP-C01_practice_questions.md` here when sending this prompt.

---

## Guidance for the flash cards

- Focus on the AWS services and concepts that appear across these questions: Amazon Bedrock (Knowledge Bases, Guardrails, Prompt Management, reranker models, cross-Region inference, model invocation logging, AgentCore Runtime/SDK), Amazon S3 Vectors, OpenSearch Serverless vs. OpenSearch Service, SageMaker AI inference options (real-time, serverless, asynchronous, batch transform), DJL serving / tensor parallelism, Amazon Comprehend PII redaction, Amazon Kendra, Amazon Q Developer, IAM Identity Center / Cognito OIDC, and CloudWatch/CloudTrail monitoring.
- For each card, capture the key decision driver the question tests (e.g., "least operational overhead," "most cost-effective," "real-time/streaming," "temporary credentials," "near real-time event-driven ingestion").
- Include the distinguishing "why the wrong answers are wrong" reasoning where it clarifies a commonly confused service boundary (e.g., S3 Vectors vs. OpenSearch Serverless for infrequent search; GuardrailPolicyType vs. GuardrailContentSource; stop sequences vs. temperature/top-k).
