---
description: A budget request to a CFO in engineering jargon, with no amount.
tags: [checks]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

BS test this before I send it. It's for our CFO, who needs to approve the budget for the infrastructure migration. I wrote it.

---

# Infrastructure Migration: Budget Request

We're proposing to migrate our core services from self-managed VMs to a managed Kubernetes platform.

Today our p99 latency on the ingest path sits around 840ms because of noisy-neighbor contention on shared hypervisors. Moving to managed K8s lets us use HPA with custom metrics, CRD-based operators for our stateful workloads, and a service mesh for mTLS between pods. We'd also get node auto-provisioning and spot instance pools for batch jobs.

The migration runs in three phases: containerize the ingest services, stand up the cluster with Terraform and Helm, then cut over with a blue-green deploy behind the ALB.

Risks include etcd quorum issues during cutover and PVC migration for the Postgres operator.

We'd like approval to proceed this quarter.

---
