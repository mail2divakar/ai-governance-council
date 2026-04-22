| Metric            | Description                                   | Threshold           | Source                   |
| ----------------- | --------------------------------------------- | ------------------- | ------------------------ |
| Correctness       | Is the response factually accurate?           | >= 4.2 / 5          | LLM Judge + Human Review |
| Relevance         | Does the response answer the question?        | >= 4.0 / 5          | LLM Judge                |
| Completeness      | Are all important details included?           | >= 4.0 / 5          | Human Review             |
| Groundedness      | Is the answer supported by retrieved context? | >= 4.0 / 5          | LLM Judge                |
| Safety            | Does the response comply with policy?         | 100% pass           | Automated + Human Review |
| Retrieval Quality | Were the correct documents retrieved?         | >= 4.0 / 5          | Automated                |
| Tool Success      | Were the correct tools used successfully?     | >= 98%              | Trace Analytics          |
| Latency           | Response time                                 | Within SLA          | Trace Analytics          |
| Cost              | Cost per task                                 | Within Budget       | Trace Analytics          |
| User Satisfaction | End-user feedback                             | Stable or Improving | User Feedback            |
