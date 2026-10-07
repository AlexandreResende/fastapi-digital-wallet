# fastapi-digital-wallet

## creating the virtual environment

> python -m venv digital-wallet  
> source digital-wallet/bin/activate  
>   
> deactivate ## deactivate the virtual environment

## installing dependencies

pip install "fastapi[standard]"

## running the project

> uvicorn main:app --reload  

## feature ideas

Features are grouped by theme, roughly ordered from easier to harder. Each lists the Python/FastAPI skills it exercises.

### 1. Foundations

- [ ] **Project structure**: split into `routers/`, `schemas/`, `models/`, `services/`, `repositories/`. *(modules, packages, separation of concerns)*
- [ ] **Configuration**: load settings from environment variables with `pydantic-settings`. *(typing, `.env` files)*
- [ ] **Pydantic schemas**: request/response models with validation (e.g. positive amounts, currency codes). *(Pydantic v2, validators)*
- [ ] **Dependency injection**: share DB sessions, current user and settings via `Depends`. *(FastAPI DI)*
- [ ] **Custom exception handlers**: consistent error responses (`InsufficientFunds`, `WalletNotFound`). *(custom exceptions, exception handlers)*

### 2. Users and authentication

- [ ] **User registration and login**: hash passwords with `argon2` or `bcrypt`. *(security basics)*
- [ ] **JWT access and refresh tokens**: OAuth2 password flow. *(`OAuth2PasswordBearer`, token expiry)*
- [ ] **Role-based access control**: `user` and `admin` roles, protected routes. *(dependencies, authorization)*
- [ ] **Email verification and password reset**: tokens with expiry. *(background tasks)*
- [ ] **Two-factor authentication (TOTP)**: e.g. with `pyotp`. *(third-party libraries)*

### 3. Wallet core

- [ ] **Create and manage wallets**: one user can have multiple wallets, each with a currency.
- [ ] **Deposit and withdraw**: with balance checks.
- [ ] **Transfer between wallets**: atomic debit and credit. *(DB transactions, rollback)*
- [ ] **Transaction history**: filter by date, type and amount. *(query params, filtering)*
- [ ] **Pagination and sorting**: offset/limit and cursor-based. *(generic types, reusable dependencies)*
- [ ] **Use `Decimal` for money**, never `float`. *(numeric precision, `decimal` module)*

### 4. Database and persistence

- [ ] **SQLAlchemy 2.0 ORM** with PostgreSQL. *(models, relationships, sessions)*
- [ ] **Alembic migrations**. *(schema versioning)*
- [ ] **Async database access**: `asyncpg` plus `AsyncSession`. *(`async`/`await`, event loop)*
- [ ] **Repository pattern**: hide persistence behind an interface. *(ABCs, `Protocol`)*
- [ ] **Optimistic and pessimistic locking**: prevent race conditions on balances. *(`SELECT ... FOR UPDATE`, version columns)*
- [ ] **Soft deletes and audit columns**: `created_at`, `updated_at`, `deleted_at`. *(mixins)*

### 5. Financial correctness

- [ ] **Idempotency keys**: avoid duplicate transfers on retries. *(headers, caching, unique constraints)*
- [ ] **Double-entry ledger**: every transaction creates balanced debit and credit entries. *(domain modeling)*
- [ ] **Transaction states**: `pending`, `completed`, `failed`, `reversed`. *(`Enum`, state machine)*
- [ ] **Refunds and reversals**.
- [ ] **Transaction limits**: daily and monthly caps per user. *(business rules, strategy pattern)*
- [ ] **Multi-currency support**: exchange rates from an external API. *(`httpx`, caching)*

### 6. Advanced features

- [ ] **Scheduled and recurring payments**: with Celery, ARQ or APScheduler. *(task queues)*
- [ ] **Payment requests**: request money from another user and accept or decline.
- [ ] **Notifications**: email or webhooks on transactions. *(background tasks, event-driven design)*
- [ ] **Webhooks with HMAC signatures**: let third parties subscribe to events. *(`hmac`, retries)*
- [ ] **Rate limiting**: protect sensitive endpoints, e.g. with Redis. *(middleware, Redis)*
- [ ] **Fraud detection rules**: flag unusual amounts or velocity. *(rule engine, design patterns)*
- [ ] **Statements export**: CSV or PDF. *(streaming responses, generators)*
- [ ] **WebSocket live balance updates**. *(`WebSocket`, connection management)*

### 7. Quality and testing

- [ ] **Unit tests** with `pytest` and fixtures. *(fixtures, parametrization)*
- [ ] **API tests** with `TestClient` / `httpx.AsyncClient`, plus dependency overrides.
- [ ] **Test database isolation**: rollback per test, or testcontainers. *(fixtures, scoping)*
- [ ] **Property-based testing** with `hypothesis` for ledger invariants.
- [ ] **Coverage** with `pytest-cov`, with a minimum threshold.
- [ ] **Concurrency tests**: many simultaneous transfers must never overdraw. *(`asyncio.gather`)*

### 8. Tooling and code quality

- [ ] **Linting and formatting**: `ruff`, plus `mypy` or `pyright` in strict mode. *(type hints)*
- [ ] **Pre-commit hooks**.
- [ ] **Dependency management**: migrate to `uv` or `poetry` with a lockfile. *(`pyproject.toml`)*
- [ ] **CI pipeline**: lint, type-check and test on every push.

### 9. Observability and operations

- [ ] **Structured logging** with request IDs. *(`logging`, `contextvars`, middleware)*
- [ ] **Health and readiness checks** that verify DB connectivity.
- [ ] **Metrics**: Prometheus endpoint. *(instrumentation)*
- [ ] **Tracing**: OpenTelemetry. *(distributed tracing)*
- [ ] **Dockerfile and docker-compose**: app, Postgres and Redis. *(containers)*
- [ ] **API versioning**: `/api/v1`, `/api/v2`. *(`APIRouter` prefixes)*

### 10. Stretch goals

- [ ] **Event sourcing**: derive balances from an append-only event log.
- [ ] **Outbox pattern** with Kafka or RabbitMQ for reliable event publishing.
- [ ] **Split into services**: separate auth, wallet and notification services.
- [ ] **GraphQL endpoint** with Strawberry.
- [ ] **Simple admin dashboard** (e.g. HTMX or React).
- [ ] **Caching layer** for balances and exchange rates, with invalidation strategy.

### Suggested order

1. Foundations, then Wallet core with in-memory storage.
2. Database and persistence, then Users and authentication.
3. Financial correctness (the most valuable section for learning).
4. Testing and tooling, in parallel with everything else.
5. Advanced features, observability, then stretch goals.