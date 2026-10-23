---
description: A long reference page whose length fits its job.
tags: [clean]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

BS test this before I publish it. It's the rate limits page in our developer docs, for engineers integrating with our API. It's my draft.

---

# Rate Limits

Every API request counts against your workspace's rate limit. Limits protect the service for everyone and are applied per workspace, not per API key.

## Limits by plan

| Plan | Requests per minute | Burst (requests per second) | Concurrent requests |
|---|---|---|---|
| Free | 60 | 5 | 2 |
| Team | 600 | 20 | 10 |
| Business | 3,000 | 50 | 25 |
| Enterprise | Custom | Custom | Custom |

The per-minute limit is a rolling 60-second window: each request counts for 60 seconds after it's made. The burst limit applies to any single second. Requests rejected with a 429 don't count.

## Response headers

Every response includes these headers:

- `X-RateLimit-Limit`: your per-minute limit.
- `X-RateLimit-Remaining`: requests left in the current window.
- `X-RateLimit-Reset`: seconds until your oldest counted request expires and frees capacity.

Read `X-RateLimit-Remaining` before batching work, and slow down as it approaches zero.

## When you hit a limit

Requests over any limit return `429 Too Many Requests` with a `Retry-After` header giving the number of seconds to wait, and a `limit` field naming which limit you hit: `per_minute`, `burst`, `concurrency` or the endpoint name. The request was not processed, so it's safe to retry after that wait.

```json
{
  "error": "rate_limited",
  "message": "Rate limit exceeded. Retry after 12 seconds.",
  "limit": "per_minute",
  "retry_after": 12
}
```

## Retrying safely

1. Wait for the longer of `Retry-After` and your backoff step. Backoff steps are 1, 2, 4 and then 8 seconds, plus a random 0 to 1 second each time. With the example above, wait 12 seconds first.
2. Stop after five attempts and surface the error to your user.

Don't retry in a tight loop: a 429 means the work wasn't done, and immediate retries only add more 429s.

## Endpoints with their own limits

Some endpoints have lower limits because they do more work per request:

- `POST /exports`: 10 per hour per workspace.
- `POST /imports`: 5 per hour per workspace.
- `GET /search`: 120 per minute, counted separately from your plan limit.

Exports and imports also count toward your plan's per-minute limit.

## Webhooks

Webhook deliveries from us to you don't count against your limits.

## Raising your limits

Team and Business workspaces can request a temporary increase for a migration or launch from the developer console under Settings, then Limits. Enterprise limits are set in your contract. Contact your account team to change them.

---
