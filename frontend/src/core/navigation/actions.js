/* @flow */

import { push } from 'connected-react-router';


function update(router: Object, parameter: string, value: ?string): Function {
    return dispatch => {
        const queryString = router.location.search;
        const params = new URLSearchParams(queryString);
        const prev = params.get(parameter);

        if (value === prev || (!value && !prev)) {
            return;
        }

        // When we change the URL, we want to remove the `string` parameter
        // because with the new results, that entity might not be available
        // anymore.
        params.delete('string');

        if (!value) {
            params.delete(parameter);
        }
        else {
            params.set(parameter, value);
        }

        dispatch(push('?' + params.toString()));
    };
}


/**
 * Update the URL with a new `string` parameter.
 *
 * This function keeps all other parameters in the URL the same.
 */
export function updateEntity(router: Object, entity: string): Function {
    return update(router, 'string', entity);
}


/**
 * Update the URL with a new `search` parameter.
 *
 * This function removes the `string` parameter from the URL if any, because
 * it is possible that after the results have changed, the currently selected
 * entity won't be available anymore.
 * It keeps all other parameters in the URL the same.
 */
export function updateSearch(router: Object, search: ?string): Function {
    return update(router, 'search', search);
}


/**
 * Update the URL with a new `status` parameter.
 *
 * This function removes the `string` parameter from the URL if any, because
 * it is possible that after the results have changed, the currently selected
 * entity won't be available anymore.
 * It keeps all other parameters in the URL the same.
 */
export function updateStatus(router: Object, status: ?string): Function {
    return update(router, 'status', status);
}


/**
 * Update the URL to open the review page for a translation.
 */
export function openReview(params: Object, translation: ?string): Function {
    return dispatch => {
        dispatch(push(`/${params.locale}/${params.project}/review/${translation}/`));
    };
}


/**
 * Update the URL to open the review list page.
 */
export function openReviewList(params: Object): Function {
    return dispatch => {
        dispatch(push(`/${params.locale}/${params.project}/review/`));
    };
}


export default {
    openReview,
    openReviewList,
    updateEntity,
    updateSearch,
    updateStatus,
};
