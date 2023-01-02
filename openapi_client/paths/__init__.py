# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    HEALTH = "/health"
    APPLICATIONS = "/applications"
    APPLICATIONS_APPLICATION_ID = "/applications/{applicationId}"
    APPLICATIONS_COINS_LIST = "/applications/coins/list"
    APPLICATIONS_APPLICATION_ID_CONTRIBUTION_TYPES = "/applications/{applicationId}/contributionTypes"
    APPLICATIONS_APPLICATION_ID_CONTRIBUTION_TYPES_NAME = "/applications/{applicationId}/contributionTypes/{name}"
    CONTRIBUTIONS = "/contributions"
    CONTRIBUTIONS_FIND_BY_REVIEWER_ID = "/contributions/findByReviewerId"
    CONTRIBUTIONS_CONTRIBUTION_ID = "/contributions/{contributionId}"
    CONTRIBUTIONS_CONTRIBUTION_ID_REVIEWS = "/contributions/{contributionId}/reviews"
    CONTRIBUTIONS_CONTRIBUTION_ID_RESOLUTIONS = "/contributions/{contributionId}/resolutions"
