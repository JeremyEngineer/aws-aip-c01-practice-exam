# AWS Certified Generative AI Developer – Professional (AIP-C01)
## Official Practice Question Set — Questions & Explanations

Source: BenchPrep Official Practice Question Set (20 questions). Each question below includes the full scenario, all answer options with their explanations, and the correct answer.

---

## Question 1
An education company built a content generation system on Amazon Bedrock. The system generates practice questions to quiz end users on a topic to test their knowledge. The system consumes a mix of curated data and scraped data in the topic domain. Reviewers must approve of the generated question-response sets before end users can access the sets. The company wants to improve the system by adding source lineage for the reviewers to verify the credibility of the content.

Which combination of steps will meet these requirements with the LEAST operational overhead? (Select TWO.)

**A.** Enable Amazon Bedrock invocation logging and correlate the logs with the data source.
*Incorrect.* Amazon Bedrock invocation logging can track model interactions. However, correlating logs with data sources would require additional operational overhead. You must manually correlate logs with data sources, or you must build an automated method. This step would capture usage data but would not help reviewers verify content credibility.

**B.** Tag FM outputs with metadata from the data source.
*Correct.* You can tag the outputs with metadata about the data sources. The generated questions are the outputs; the curated and scraped data are the data sources. This provides direct traceability between generated content and its origins, gives reviewers immediate access to source information, and is a direct, automated way to track sources by injecting metadata during processing.

**C.** Register the curated and scraped input datasets with AWS Glue Data Catalog.
*Correct.* You can register input datasets by using Data Catalog to create a searchable inventory of data sources. Reviewers can use this to verify the origin and credibility of source material. It uses built-in features of a managed service and provides structured metadata management with minimal operational overhead.

**D.** Use Amazon SageMaker Clarify to explain model predictions.
*Incorrect.* SageMaker Clarify is designed for model explainability and bias detection, not source lineage tracking.

**E.** Use AWS CloudTrail to log reviewer feedback actions.
*Incorrect.* CloudTrail logs AWS API calls and can track reviewer actions like approval/rejection, but does not provide source lineage of the generated content.

**Correct Answer: B, C**

---

## Question 2
A company is implementing a systematic evaluation process for a newly deployed FM in Amazon Bedrock. The company wants to replace an existing model in production with a new model. The change is dependent on the new model demonstrating better performance. The company must follow a sequential validation process. Each step must be reviewed and approved before proceeding.

Select and order each step (Select and order FIVE):

1. Define evaluation metrics for relevance, factual accuracy, and fluency.
2. Create a test dataset with diverse scenarios and edge cases.
3. Conduct A/B testing to compare the new model against the existing production model.
4. Implement automated quality gates by using AWS Step Functions.
5. Analyze the results and generate a comprehensive evaluation report.

**Correct Order: 1 → 2 → 3 → 4 → 5**

---

## Question 3
A company needs secure authentication for a third-party application that uses Amazon Bedrock. The solution must integrate with the company's existing identity provider (IdP), maintain comprehensive audit logs of authentication and API calls, eliminate long-lived credentials, and provide temporary access to Amazon Bedrock.

Which solutions will meet these requirements? (Select TWO.)

**A.** Implement an OpenID Connect (OIDC) integration with Amazon Cognito. Configure it to authenticate users through the IdP and exchange tokens for temporary AWS credentials to access Amazon Bedrock.
*Correct.* Cognito with OIDC authenticates users through the existing IdP, exchanges identity tokens for temporary AWS credentials (eliminating long-lived credentials), and provides comprehensive logging through AWS CloudTrail.

**B.** Configure an Amazon API Gateway Lambda authorizer to validate credentials against LDAP and issue signed JWTs for Amazon Bedrock access.
*Incorrect.* Does not meet the requirement for temporary AWS credentials and requires custom development; does not use built-in identity federation.

**C.** Create IAM users for each employee, assign permissions through IAM policies, and rotate credentials with AWS Secrets Manager.
*Incorrect.* IAM users rely on persistent access keys (long-lived credentials), do not integrate with the existing IdP, and do not provide temporary access.

**D.** Create an IAM role and configure federation by using AWS STS AssumeRole. Store the application's IAM user credentials in the application configuration.
*Incorrect.* Storing IAM user credentials violates the requirement to eliminate long-lived credentials and does not properly integrate with the IdP.

**E.** Deploy AWS IAM Identity Center with SAML federation to the IdP. Configure custom permission sets that grant access to Amazon Bedrock.
*Correct.* IAM Identity Center with SAML federation integrates with the IdP, eliminates long-lived credentials with temporary security credentials, and provides audit logging through CloudTrail.

**Correct Answer: A, E**

---

## Question 4
A company is developing a RAG application by using Amazon Bedrock. The application processes customer support documents. Initially, the application retrieves many relevant documents. However, users report that the most relevant information often appears lower in the results. The company wants to improve the relevance ranking of retrieved results to ensure that the most useful information appears first.

Which combination of steps will improve the relevance of retrieved results with MINIMAL operational overhead? (Select TWO.)

**A.** Configure Amazon OpenSearch Serverless with the Amazon Bedrock Knowledge Bases plugin. Use OpenSearch's Learning to Rank feature for relevance scoring.
*Incorrect.* Learning to Rank is an open source plugin requiring custom relevance scoring and trained/maintained custom models — more operational overhead than Bedrock built-in features.

**B.** Create an Amazon Aurora PostgreSQL database with pgvector and a custom similarity scoring algorithm combining vector distances with metadata.
*Incorrect.* Requires custom development to implement scoring and maintain the vector database — more operational overhead.

**C.** Use Amazon Bedrock reranker models with Amazon OpenSearch Service to reorder retrieved results based on semantic relevance to the query.
*Correct.* Bedrock reranker models are purpose-built to improve relevance; they calculate query-document relevance scores and reorder results so the most relevant information appears first.

**D.** Use Amazon SageMaker JumpStart FMs with Amazon Kendra Intelligent Ranking to create custom relevancy scoring algorithms.
*Incorrect.* Bedrock already provides built-in reranking optimized for FM integration; this approach is more complex and less integrated.

**E.** Use Knowledge Bases with hybrid search capabilities and Amazon OpenSearch Serverless to combine vector embeddings with keyword matching.
*Correct.* Hybrid search combines semantic vector embeddings with keyword matching to improve retrieval relevance using OpenSearch Serverless as the vector store.

**Correct Answer: C, E**

---

## Question 5
A financial services company is developing a research agent that processes complex financial data queries. The company must deploy existing Python agent code to Amazon Bedrock AgentCore Runtime. The company wants to reduce infrastructure management overhead and operational complexity. The agent must handle quick data lookups (sub-second responses) and comprehensive research report generation (streaming responses over several minutes). The solution must automatically manage HTTP server configuration, endpoint routing, and health monitoring.

Which deployment approaches will meet these requirements with MINIMAL operational overhead? (Select TWO.)

**A.** Implement a FastAPI server with a configuration of /invocations and /ping endpoints and container orchestration.
*Incorrect.* FastAPI requires manual configuration of endpoints, JSON/streaming handling, Dockerfiles, and deployment orchestration — increases operational overhead.

**B.** Implement the AgentCore SDK with the @app.entrypoint decorator to automatically handle server setup and endpoint management.
*Correct.* The SDK automatically creates an HTTP server on port 8080, implements the required /invocations and /ping endpoints, handles content types/response formats, and supports both JSON and streaming responses without manual configuration.

**C.** Deploy the agent on Amazon ECS on AWS Fargate by using a custom container image running the AgentCore SDK.
*Incorrect.* Requires building/maintaining Dockerfiles, managing container images, and task definitions; no automatic HTTP server setup/health monitoring.

**D.** Deploy the agent on Amazon SageMaker AI real-time endpoints by using a custom inference container.
*Incorrect.* Increases infrastructure overhead: building Docker images, configuring inference server, auto scaling policies, container health monitoring.

**E.** Deploy the agent by using the AgentCore starter toolkit for automated packaging, containerization, and deployment workflows.
*Correct.* The starter toolkit automates packaging, ARM64 container builds, ECR repository creation/image push, and deployment via CreateAgentRuntime — minimal operational overhead.

**Correct Answer: B, E**

---

## Question 6
A company is building a diagnostic imaging application. It needs to perform similarity searches across 50 million images to assist with diagnosing and treating patients. The application processes new images daily and performs similarity searches infrequently when users need to find similar cases. The company wants a cost-effective solution with responsive search performance and no infrastructure management.

Which solution will meet these requirements MOST cost-effectively?

**A.** Store image vectors in Amazon OpenSearch Serverless and use vector search for similarity searches.
*Incorrect.* OpenSearch Serverless is optimized for high-throughput, low-latency, frequent searches; you pay for provisioned capacity that stays underutilized with infrequent searches.

**B.** Use Amazon DynamoDB to store image vectors and implement custom similarity search logic with AWS Lambda.
*Incorrect.* DynamoDB has no built-in vector similarity search; custom Lambda logic introduces latency and compute costs.

**C.** Create an Amazon S3 vector bucket with vector indexes to store image embeddings and perform similarity searches.
*Correct.* S3 Vectors is fully managed and serverless, supports up to billions of vectors, suits infrequent searches, requires no infrastructure provisioning, and you pay only for what you use — cost-effective for 50M image vectors.

**D.** Store image vectors in Amazon RDS for PostgreSQL and use the pgvector extension.
*Incorrect.* RDS requires provisioning/managing database instances (does not meet "no infrastructure management") and is not cost-effective for infrequent workloads.

**Correct Answer: C**

---

## Question 7
An ecommerce company uses Amazon Bedrock to generate product descriptions and recommendations. The application resides in a single AWS Region. During peak periods it receives "Too many requests, please wait before trying again." The company must increase invocation throughput during peak periods without additional operational overhead, maintain compatibility with the existing Amazon Bedrock API, and use the same FM.

Which solution will meet these requirements in the MOST cost-effective way?

**A.** Create an AWS Lambda function to invoke the model with the original Region as default and fall back to a secondary Region.
*Incorrect.* A Lambda intermediary must be managed/maintained, increasing cost and operational overhead vs. a built-in feature.

**B.** Use cross-Region inference to distribute traffic across multiple Regions within a geographic area.
*Correct.* Cross-Region inference automatically distributes traffic across multiple Regions within your geographic area to process inference requests.

**C.** Use prompt routing to distribute traffic across multiple FMs from the same family.
*Incorrect.* Intelligent prompt routing requires at least two different models from the same family; the company must use the same FM.

**D.** Use provisioned throughput to provision a higher level of throughput for the FM.
*Incorrect.* Provisioned throughput suits consistent usage, not occasional peak periods.

**Correct Answer: B**

---

## Question 8
A company uses an AI assistant to answer customer questions based on internal documents. It wants new documents included in responses as soon as possible and deleted documents excluded as soon as possible. Documents are stored in Amazon S3; the AI assistant uses Amazon Bedrock Knowledge Bases with S3 as the data source for the RAG vector store. A GenAI developer must create a scalable, event-driven, and resilient solution.

Which solution will meet these requirements?

**A.** Configure EventBridge Scheduler to run every 5 minutes and invoke a Lambda that tracks S3 changes and calls IngestKnowledgeBaseDocuments/DeleteKnowledgeBaseDocuments.
*Incorrect.* Time-based, not near real-time; tracking changes in Lambda is not operationally efficient.

**B.** Configure S3 Event Notifications to invoke a Lambda on object-created/object-deleted events that calls IngestKnowledgeBaseDocuments/DeleteKnowledgeBaseDocuments.
*Incorrect.* No buffering/retry support; S3 directly invoking Lambda can fail under high load due to synchronous invocation limits.

**C.** Configure S3 Event Notifications to send object-created/object-deleted events to an Amazon SQS queue; a Lambda polls the queue and calls IngestKnowledgeBaseDocuments/DeleteKnowledgeBaseDocuments.
*Correct.* SQS buffers between S3 events and Lambda, handles traffic spikes, provides automatic retries, and ensures no updates are missed — scalable and resilient.

**D.** Configure EventBridge Scheduler to run every 5 minutes and invoke a Lambda that syncs S3 with the knowledge base via StartIngestionJob.
*Incorrect.* Inefficient periodic full scanning, introduces delays, not event-driven.

**Correct Answer: C**

---

## Question 9
A financial services company operates RAG for an application answering questions using internal market analysis reports. It uses Amazon Bedrock for the embedding model and an Amazon OpenSearch Service cluster as the vector store; an AWS Lambda function performs embedding and search logic. After a code update, the app returns generic responses (e.g., "no relevant information found") even for previously answerable questions. CloudWatch Logs shows no errors, X-Ray confirms successful FM invocation, the OpenSearch cluster is healthy, and query latency is normal.

What is the cause of this issue?

**A.** The document embeddings in OpenSearch were deleted during the update and not re-indexed.
*Incorrect.* Deleted embeddings would appear in logs or cause failed queries; there are no errors/latency issues, so documents are still retrieved.

**B.** The Lambda function's IAM role is missing bedrock:InvokeModel permission.
*Incorrect.* The model is invoked successfully; a missing permission would throw an access error.

**C.** The Amazon Bedrock FM temperature parameter was increased.
*Incorrect.* High temperature affects generation randomness, not retrieval; the issue is a retrieval failure.

**D.** The updated Lambda function uses a different version of the embedding model.
*Correct.* Embedding drift — query embeddings generated with a different model than the one used to index documents causes a vector-space mismatch and ineffective retrieval.

**Correct Answer: D**

---

## Question 10
A company is developing an AI assistant that processes customer data with Amazon Bedrock. It has multiple guardrails: prompt injection detection, sensitive information filtering, and denied topic blocking. When a query is blocked, a GenAI developer needs detailed analysis of which specific guardrail rule was invoked and why content was flagged, then must fine-tune guardrail configurations and distinguish legitimate queries from security threats.

Which configuration provides the MOST detailed analysis of guardrail decision-making for content filtering?

**A.** Enable Amazon Bedrock model evaluation with automated evaluation jobs including guardrail assessment metrics; test prompt injection resistance with company-specific test cases; analyze via the evaluation dashboard.
*Incorrect.* Model evaluation is for measurable tests/reports, not used during inference.

**B.** Enable model invocation logging; configure CloudWatch alarms on InvocationsIntervened filtered by GuardrailContentSource; analyze with CloudWatch Insights.
*Incorrect.* Invocation logging logs input/output/metadata but not guardrail intervention details.

**C.** Configure guardrail tracing with {"trace": "enabled"}; monitor InvocationsIntervened filtered by GuardrailContentSource to identify whether input prompts or output responses triggered interventions.
*Incorrect.* GuardrailContentSource distinguishes input vs. output but not which guardrail layer intervened.

**D.** Configure guardrail tracing with {"trace": "enabled"}; monitor InvocationsIntervened filtered by GuardrailPolicyType dimensions: ContentPolicy, TopicPolicy, and SensitiveInformationPolicy.
*Correct.* GuardrailPolicyType provides detailed information on which policy intervened, enabling informed decisions based on specific metrics.

**Correct Answer: D**

---

## Question 11
A financial services company wants to develop a mobile app to help users with account inquiries and general account information. It has a large amount of email exchange data between customers and support staff to use as source material. The data is stored in an Amazon S3 bucket and contains personally identifiable information (PII) that should not appear in search results.

Which solution will meet these requirements?

**A.** Use Amazon Kendra for enterprise search of the email data and integrate with an Amazon Bedrock FM, using a system prompt to identify and remove PII during query processing.
*Incorrect.* System prompts cannot reliably/consistently remove PII and can be jailbroken — not secure for sensitive financial data.

**B.** Use Amazon Comprehend to detect and redact PII from the email data in S3, and integrate Comprehend with Amazon Kendra to enable enterprise search of the processed data.
*Correct.* Comprehend detects/redacts sensitive information from text data; Kendra provides managed enterprise search of the processed data for conversational AI integration.

**C.** Use Amazon Textract to extract text, Amazon Macie to scan for PII in S3, and integrate Textract and S3 with Amazon Kendra.
*Incorrect.* Macie is for data discovery/security assessment, not PII redaction for GenAI; Textract is optimized for scanned documents, not raw email text.

**D.** Use Amazon Comprehend to detect and redact PII, and integrate with Amazon DocumentDB for database queries.
*Incorrect.* DocumentDB requires custom search development and lacks NLP for natural-language user interactions; not designed for enterprise search.

**Correct Answer: B**

---

## Question 12
A company wants to create an application to analyze fashion trends. The application must analyze videos and photos from public fashion shows to understand style elements and trends. The solution must store extracted information and provide a dashboard that summarizes fashion trends.

Which solution will meet these requirements with the LEAST operational overhead?

**A.** Use Amazon EventBridge to trigger Lambda functions that use Amazon QuickSight Q to analyze videos/photos; store results in S3; deploy a QuickSight dashboard with ML-powered trend analysis.
*Incorrect.* QuickSight Q answers questions about data already in a dashboard; it cannot analyze videos/photos.

**B.** Use AWS Step Functions to process videos/photos using Amazon Bedrock multimodal FMs; store results in S3; use an Amazon QuickSight dashboard to visualize trends.
*Correct.* Bedrock multimodal FMs (e.g., Amazon Nova Pro, Claude Sonnet) directly analyze videos/photos and extract style/trend info without custom model development; Step Functions coordinates the workflow; QuickSight builds dashboards serverlessly — least operational overhead.

**C.** Use Amazon Rekognition Custom Labels to train a custom model; store results in DynamoDB; create an Amazon Managed Grafana dashboard with custom plugins.
*Incorrect.* Requires custom model training/maintenance and custom Grafana plugin development — more overhead.

**D.** Use an Anthropic Claude model in Bedrock to analyze text descriptions, use Stable Diffusion for image analysis, store results in OpenSearch Service, and create a Managed Grafana dashboard.
*Incorrect.* Requires managing an OpenSearch cluster, coordinating multiple FMs, and custom visualizations; also analyzes text descriptions rather than the visual content directly.

**Correct Answer: B**

---

## Question 13
A financial services company needs Amazon Bedrock to create an AI assistant for customer support reps across multiple business units. A GenAI developer must ensure prompt templates are governed through approval workflows. The company requires comprehensive logging of all model invocations with a 7-year retention period for regulatory compliance.

Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

**A.** Use Amazon Bedrock Prompt Management with multi-stage approval workflows and IAM policies that require multi-party authorization.
*Correct.* Prompt Management securely creates, parameterizes, versions, and approves prompt templates with multi-stage approvals, access roles, version control, and collaboration — suitable for diverse business units and governance.

**B.** Store prompt templates in DynamoDB tables with composite keys partitioned by business unit; use IAM policies and item-level permissions for approvals.
*Incorrect.* Requires custom development for approval workflows/access control — increases overhead.

**C.** Set up EventBridge rules to capture model invocation events, route to CloudWatch Logs by business unit, export to S3, and enable S3 Object Lock compliance mode for 7 years.
*Incorrect.* Requires custom configuration/maintenance and creates failure points; does not provide the comprehensive audit trail needed.

**D.** Enable AWS CloudTrail data events for all Bedrock APIs, deliver to CloudTrail Lake with 7-year retention, tag events with business unit ID, and query with CloudTrail Lake.
*Incorrect.* CloudTrail captures only API metadata, not actual prompt content/model responses needed for regulatory reconstruction.

**E.** Enable Amazon Bedrock model invocation logging with Amazon S3 as the destination; enable S3 Object Lock compliance mode for 7 years; create separate prefixes per business unit.
*Correct.* Built-in invocation logging with minimal setup; S3 Object Lock compliance mode provides immutable storage enforcing 7-year retention; S3 prefixes provide business-unit segregation.

**Correct Answer: A, E**

---

## Question 14
A company is implementing AI governance policies requiring all FM interactions to be secured with guardrails. The company configures Amazon Bedrock guardrails and must ensure that all InvokeModel and Converse API calls to FMs apply the guardrails.

Which solution will enforce guardrail compliance for the API calls in the MOST operationally efficient way?

**A.** Configure IAM policies for InvokeModel/Converse with both bedrock:GuardrailIdentifier and bedrock:PromptRouterArn condition keys; require prompt router validation.
*Incorrect.* PromptRouterArn filters access by prompt router and is unrelated to guardrail enforcement; adds complexity without benefit.

**B.** Create a Lambda function that validates and enforces guardrails before proxying requests to Bedrock, used as the exclusive endpoint.
*Incorrect.* Adds a failure point/bottleneck and custom code maintenance — less efficient than built-in capabilities.

**C.** Store guardrail identifiers in Systems Manager Parameter Store; a Lambda retrieves the identifier each time before calling Bedrock.
*Incorrect.* Retrieving the identifier per call adds overhead/latency and Lambda maintenance.

**D.** Configure IAM policies for InvokeModel/Converse with the bedrock:GuardrailIdentifier condition key, applied to all IAM roles that access Bedrock FMs.
*Correct.* IAM policies with the GuardrailIdentifier condition key centrally and efficiently enforce guardrail compliance consistently across all relevant API calls.

**Correct Answer: D**

---

## Question 15
A GenAI developer is building a virtual assistant using an Anthropic Claude model on Amazon Bedrock. The application sends user queries and expects conversational responses. The developer wants to configure the application to stop generating output after a specific phrase is generated in the response.

Which solution will meet these requirements?

**A.** Add the trigger phrase "stop at this phrase" in the user prompt.
*Incorrect.* Relies on the model following instructions, which it might not do — not reliable.

**B.** Use the stop sequences parameter in the inference call to specify a trigger phrase.
*Correct.* The stop sequences parameter is a built-in API mechanism that stops the model after generating certain key phrases — directly controls output generation.

**C.** Use the top-k parameter to control the diversity of tokens in the output.
*Incorrect.* top-k controls sampling diversity, not stopping at specific phrases.

**D.** Use the temperature parameter to control the likelihood of the phrase appearing.
*Incorrect.* Temperature controls randomness/creativity, not the stopping point.

**Correct Answer: B**

---

## Question 16
A cross-functional team is developing a generative AI application using AWS services. The team needs to optimize developer productivity, enforce consistent integration patterns, automate performance tuning, and accelerate AI testing across multiple business units. The team wants to use Amazon Q Developer to accelerate development workflows and maintain application quality.

Which combination of steps will meet these requirements? (Select TWO.)

**A.** Use Amazon Q Developer to analyze code for security best practices, with mandatory manual security-team approval of all code changes before integration.
*Incorrect.* Mandatory manual approval of all changes creates a bottleneck and does not accelerate workflows or automate tuning/testing.

**B.** Use Amazon Q Developer to retrospectively analyze and document common integration patterns across business units' code bases.
*Incorrect.* Reactive retrospective analysis fails to use real-time assistance for generation, refactoring, and testing.

**C.** Configure Amazon Q Developer to automatically generate and refactor integration code snippets, provide targeted API usage guidance, and suggest performance optimizations for AI components, applying changes across the modular code base.
*Correct.* Provides automatic code generation, refactoring, targeted API recommendations, and performance optimization to increase productivity and reduce integration errors.

**D.** Incorporate Amazon Q Developer to resolve coding issues during merge requests, reserving most refactoring/optimization for periodic manual review cycles.
*Incorrect.* Limits use to merge/review stages and infrequent manual cycles — does not optimize core benefits and slows resolution.

**E.** Integrate Amazon Q Developer automated unit and integration test generation features into the team's CI/CD pipelines.
*Correct.* Embedding automated test generation into CI/CD continuously validates components, ensuring velocity, ongoing quality, and early defect detection.

**Correct Answer: C, E**

---

## Question 17
A GenAI developer deployed a fine-tuned LLM to an Amazon SageMaker AI endpoint, using the default serving configuration for continuous batching with the AMI including the Deep Java Library (DJL). The model is served on GPU-based EC2 instances, each with 8 GPUs. As the model scales to production, many instances are needed to meet demand, and the developer wants to avoid increased costs from overutilization. Logs show the maximum I/O sequence length in real requests is 10x smaller than configured, current concurrency per instance is low, and profiling shows the model's weights and activations fit entirely within 4 GPUs.

Which combination of steps can improve resource utilization? (Select TWO.)

**A.** Increase the number of SageMaker AI instances and spread requests more evenly.
*Incorrect.* Does not improve concurrency or decrease GPU memory footprint; explore serving property configurations instead.

**B.** Reduce the model's maximum sequence length to provide a higher rolling batch size for each GPU.
*Correct.* With DJL you can reduce max sequence length to free memory for larger batch sizes, increasing throughput and concurrency per instance.

**C.** Enable speculative decoding to reduce response latency for each request.
*Incorrect.* Speculative decoding improves latency, not resource utilization.

**D.** Use tensor parallelism with a degree of 4 to deploy two model replicas for each instance.
*Correct.* Since weights/activations fit within 4 GPUs, changing the tensor parallel configuration creates multiple model copies in the same instance (two replicas across 8 GPUs).

**E.** Split the model across all 8 GPUs by using a tensor parallelism degree of 8 to improve memory efficiency.
*Incorrect.* Degree of 8 serves only one model replica across all 8 GPUs, leaving half the capacity underutilized since the model fits in 4 GPUs.

**Correct Answer: B, D**

---

## Question 18
A GenAI developer is implementing a solution to create images from text descriptions. The developer successfully tested a pre-trained Hugging Face model using Amazon SageMaker JumpStart and now needs to deploy it so users can generate images on demand. The solution must use GPUs for inference, handle text datasets up to 50 MB with image descriptions, and provide responses within 15 minutes.

Which deployment strategy will meet these requirements?

**A.** Deploy a SageMaker Asynchronous Inference endpoint using an accelerated computing instance type; create a Lambda for on-demand invocation.
*Correct.* Asynchronous endpoints support long-running inference up to 15 minutes, efficiently manage compute, support GPU instances, handle large datasets (up to 1 GB), and scale based on usage.

**B.** Deploy a SageMaker Serverless Inference endpoint using a general purpose instance type; create a Lambda for invocation.
*Incorrect.* Serverless inference does not support the GPU instances needed for efficient image generation.

**C.** Deploy a SageMaker Real-Time Inference endpoint using an accelerated computing instance type; create a Lambda for invocation.
*Incorrect.* Real-time endpoints have dataset limits up to 25 MB — does not meet the 50 MB requirement.

**D.** Create a SageMaker AI batch transform job using an accelerated computing instance type; create a Lambda to start the job.
*Incorrect.* Batch transform is for offline batch processing, not on-demand individual requests, and does not support responses within 15 minutes.

**Correct Answer: A**

---

## Question 19
A news media company wants to develop a content conformance tool that automatically reviews and adjusts articles to ensure compliance with a style guide. Journalists need a web-based article editor providing real-time analysis upon request. When journalists click an "analyze" button, the system should immediately begin providing suggested revisions through the editor interface. Articles are tagged with content categories in metadata (e.g., news, sports, editorial). The company wants to use an Amazon Bedrock FM to analyze content and provide immediate feedback.

Which architecture will meet these requirements with the LEAST operational overhead?

**A.** Implement an SQS queue for article ingestion; Step Functions to process content; Lambda to determine category from metadata and invoke Bedrock with style guide prompts; store results in DynamoDB; API Gateway WebSocket API for real-time streaming.
*Incorrect.* SQS requires polling, introducing latency — does not provide immediate feedback when journalists click "analyze."

**B.** Deploy an API Gateway WebSocket API linked to a Lambda that reads the content category from metadata, routes to the appropriate Bedrock model, uses Bedrock Prompt Management to enforce style guide rules, and uses the Bedrock streaming API to return suggestions in real time.
*Correct.* WebSocket API provides real-time bidirectional communication; Lambda reads metadata for routing; Prompt Management manages style guide rules; the streaming API delivers suggestions immediately — minimal infrastructure management.

**C.** Create an API Gateway REST API with Lambda function URLs for response streaming using chunked transfer encoding.
*Incorrect.* REST APIs are not suitable for long-lived real-time streaming connections; size limits and timeouts produce a poor experience.

**D.** Configure an Application Load Balancer with Amazon ECS tasks running custom containers implementing routing/style checking, using Bedrock streaming and WebSocket connections.
*Incorrect.* Running custom containers on ECS requires managing infrastructure, scaling, and deployment — more operational effort than serverless.

**Correct Answer: B**

---

## Question 20
A company runs a question-answering application that uses an Amazon Bedrock knowledge base ingesting documents from multiple Amazon S3 buckets. The company needs to monitor the data ingestion process to identify and troubleshoot issues with document processing.

Which solution will meet these requirements to monitor knowledge base operations?

**A.** Configure knowledge base logging with Amazon CloudWatch Logs as the destination; use CloudWatch Logs Insights to query for failed document processing.
*Correct.* Bedrock knowledge bases support built-in logging to CloudWatch Logs that tracks file status during ingestion (successfully ingested, ignored, or failed). Logs Insights can query for statuses like RESOURCE_IGNORED, EMBEDDING_FAILED, or INDEXING_FAILED.

**B.** Enable Amazon CloudWatch Application Signals to automatically detect and alert on knowledge base performance issues.
*Incorrect.* Application Signals monitors application performance/health, not knowledge base ingestion; it does not integrate with Bedrock knowledge base monitoring.

**C.** Enable AWS CloudTrail to track all API calls related to knowledge base operations and document ingestion.
*Incorrect.* CloudTrail tracks API calls but not the document-level processing information needed to troubleshoot ingestion issues.

**D.** Implement Amazon Bedrock model invocation logging to capture detailed metrics about document processing and embedding generation.
*Incorrect.* Model invocation logging captures model API calls/inference requests, not knowledge base document ingestion processes.

**Correct Answer: A**
