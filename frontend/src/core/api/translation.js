/* @flow */

import APIBase from './base';


export default class TranslationAPI extends APIBase {
    /**
     * Add or update a translation.
     *
     * If a similar translation already exists, update it with the new data.
     * Otherwise, create it.
     */
    updateTranslation(
        entity: number,
        translation: string,
        locale: string,
        pluralForm: number,
        original: string
    ) {
        const csrfToken = this.getCSRFToken();

        const payload = new URLSearchParams();
        payload.append('entity', entity.toString());
        payload.append('translation', translation);
        payload.append('locale', locale);
        payload.append('plural_form', pluralForm.toString());
        payload.append('original', original);
        payload.append('csrfmiddlewaretoken', csrfToken);

        const headers = new Headers();
        headers.append('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
        headers.append('X-Requested-With', 'XMLHttpRequest');
        headers.append('X-CSRFToken', csrfToken);

        return this.fetch('/update/', 'POST', payload, headers);
    }

    _changeStatus(url: string, id: number, resource: string) {
        const csrfToken = this.getCSRFToken();

        const payload = new URLSearchParams();
        payload.append('translation', id.toString());

        if (resource !== 'all') {
            payload.append('paths[]', resource);
        }

        const headers = new Headers();
        headers.append('X-Requested-With', 'XMLHttpRequest');
        headers.append('X-CSRFToken', csrfToken);

        return this.fetch(url, 'POST', payload, headers);
    }

    approve(id: number, resource: string) {
        return this._changeStatus('/approve-translation/', id, resource);
    }

    unapprove(id: number, resource: string) {
        return this._changeStatus('/unapprove-translation/', id, resource);
    }

    reject(id: number, resource: string) {
        return this._changeStatus('/reject-translation/', id, resource);
    }

    unreject(id: number, resource: string) {
        return this._changeStatus('/unreject-translation/', id, resource);
    }

    async get(id: string) {
        const query = `{
            translation(
                id: "${id}",
            ) {
                string
                date
                id
                pluralForm
                active
                entity {
                    id
                    string
                    comment
                    resource {
                        path
                    }
                }
                user {
                    firstName
                }
                comments {
                    content
                    date
                    author {
                        username
                    }
                }
            }
        }`;
        const payload = new URLSearchParams();
        payload.append('query', query);

        const headers = new Headers();
        headers.append('X-Requested-With', 'XMLHttpRequest');

        return await this.fetch('/graphql/', 'GET', payload, headers);
    }

    async getUnreviewed(locale: string, project: string) {
        const query = `{
            unreviewedTranslations(
                locale: "${locale}",
                project: "${project}"
            ) {
                string
                date
                id
                pluralForm
                entity {
                    id
                    string
                }
                user {
                    firstName
                }
            }
        }`;
        const payload = new URLSearchParams();
        payload.append('query', query);

        const headers = new Headers();
        headers.append('X-Requested-With', 'XMLHttpRequest');

        return await this.fetch('/graphql/', 'GET', payload, headers);
    }
}
