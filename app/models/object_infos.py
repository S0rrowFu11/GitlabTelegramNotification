from enum import Enum


class ObjectType(Enum):
    NOTE = "note"
    ISSUE_NOTEABLE_TYPE = "Issue"
    MERGE_REQUEST_NOTEABLE_TYPE = "MergeRequest"
    ISSUE = "issue"
    MERGE_REQUEST = "merge_request"
    PIPELINE = "pipeline"
    FAILED_STATUS = "failed"
