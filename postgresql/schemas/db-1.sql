create schema tg_gitlab;
create table tg_gitlab.telegram_gitlab (
 id SERIAL,
 created_at TIMESTAMPTZ default NOW(),
 updated_at TIMESTAMPTZ default NOW(),
 telegram_id BIGINT not null,
 gitlab_id bigint not null,
 unique(telegram_id, gitlab_id)
);