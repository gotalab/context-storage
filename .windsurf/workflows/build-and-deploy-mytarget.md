---
description: Use this workflow to safely deploy the application to production.
---

1. Run tests to verify everything works

npm run test

2. Build the production package

npm run build

3. Deploy to production server

npm run deploy:prod

4. Verify deployment succeeded

curl https://your-app-url.com/health