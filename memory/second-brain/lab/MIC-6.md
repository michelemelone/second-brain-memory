# MIC-6: Make memory.beedme.online reachable

- Project: Second Brain
- Status: done
- Priority: high
- Agent: Sirius
- Parent: MIC-5
- Updated: 2026-11-17

## Request

Done by the agent: .env, second-brain.service started on 192.168.12.200:3739. For Michele: (1) Nginx Proxy Manager, host memory.beedme.online: change the port 3738 to 3739 (scheme http, host 192.168.12.200); (2) run: sudo ufw allow 3739/tcp (same as was done for port 3000), then test from the proxy container. Then open [https://memory.beedme.online](https://memory.beedme.online) and log in through Cloudflare Access.

## Last report of the agent

(none)
