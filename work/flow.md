# 認証フロー（Cognito → Django）

```mermaid
sequenceDiagram
    autonumber
    actor User as ユーザー(ブラウザ/Next.js)
    participant FE as Frontend(Next.js)
    participant Cognito as AWS Cognito Hosted UI
    participant Django as Django(backend)
    participant DB as MySQL

    User->>FE: 「ログイン」クリック
    FE->>Cognito: /authorize へリダイレクト
    Cognito-->>User: ログイン画面表示
    User->>Cognito: 認証
    Cognito-->>FE: redirect_uri?code=...&state=...
    FE->>Django: /auth/callback?code=...&state=...
    Django->>Cognito: /oauth2/token でトークン交換（本番）
    Django->>DB: app_users を upsert（sub, email…）
    Django-->>User: セッション発行 & リダイレクト(/onboarding)
