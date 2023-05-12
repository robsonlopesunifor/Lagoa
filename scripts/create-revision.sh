NEXT_ID=`ls alembic/versions/* | grep -P '/revision_\d{4}.*\.py$' | wc -l`
alembic revision --autogenerate --rev-id=`printf "revision_%04d" ${NEXT_ID}`