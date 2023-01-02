import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.health import Health
from openapi_client.apis.paths.applications import Applications
from openapi_client.apis.paths.applications_application_id import ApplicationsApplicationId
from openapi_client.apis.paths.applications_coins_list import ApplicationsCoinsList
from openapi_client.apis.paths.applications_application_id_contribution_types import ApplicationsApplicationIdContributionTypes
from openapi_client.apis.paths.applications_application_id_contribution_types_name import ApplicationsApplicationIdContributionTypesName
from openapi_client.apis.paths.contributions import Contributions
from openapi_client.apis.paths.contributions_find_by_reviewer_id import ContributionsFindByReviewerId
from openapi_client.apis.paths.contributions_contribution_id import ContributionsContributionId
from openapi_client.apis.paths.contributions_contribution_id_reviews import ContributionsContributionIdReviews
from openapi_client.apis.paths.contributions_contribution_id_resolutions import ContributionsContributionIdResolutions

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HEALTH: Health,
        PathValues.APPLICATIONS: Applications,
        PathValues.APPLICATIONS_APPLICATION_ID: ApplicationsApplicationId,
        PathValues.APPLICATIONS_COINS_LIST: ApplicationsCoinsList,
        PathValues.APPLICATIONS_APPLICATION_ID_CONTRIBUTION_TYPES: ApplicationsApplicationIdContributionTypes,
        PathValues.APPLICATIONS_APPLICATION_ID_CONTRIBUTION_TYPES_NAME: ApplicationsApplicationIdContributionTypesName,
        PathValues.CONTRIBUTIONS: Contributions,
        PathValues.CONTRIBUTIONS_FIND_BY_REVIEWER_ID: ContributionsFindByReviewerId,
        PathValues.CONTRIBUTIONS_CONTRIBUTION_ID: ContributionsContributionId,
        PathValues.CONTRIBUTIONS_CONTRIBUTION_ID_REVIEWS: ContributionsContributionIdReviews,
        PathValues.CONTRIBUTIONS_CONTRIBUTION_ID_RESOLUTIONS: ContributionsContributionIdResolutions,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HEALTH: Health,
        PathValues.APPLICATIONS: Applications,
        PathValues.APPLICATIONS_APPLICATION_ID: ApplicationsApplicationId,
        PathValues.APPLICATIONS_COINS_LIST: ApplicationsCoinsList,
        PathValues.APPLICATIONS_APPLICATION_ID_CONTRIBUTION_TYPES: ApplicationsApplicationIdContributionTypes,
        PathValues.APPLICATIONS_APPLICATION_ID_CONTRIBUTION_TYPES_NAME: ApplicationsApplicationIdContributionTypesName,
        PathValues.CONTRIBUTIONS: Contributions,
        PathValues.CONTRIBUTIONS_FIND_BY_REVIEWER_ID: ContributionsFindByReviewerId,
        PathValues.CONTRIBUTIONS_CONTRIBUTION_ID: ContributionsContributionId,
        PathValues.CONTRIBUTIONS_CONTRIBUTION_ID_REVIEWS: ContributionsContributionIdReviews,
        PathValues.CONTRIBUTIONS_CONTRIBUTION_ID_RESOLUTIONS: ContributionsContributionIdResolutions,
    }
)
