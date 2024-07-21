import { fetchAppDetail } from '@/service/apps'
import type { App } from '@/types/app'

const buildDeploymentUrl = (app: App): string => {
  const { app_base_url: appBaseURL = '', access_token: accessToken = '' } = app.site ?? {}
  const appMode = (app.mode !== 'completion' && app.mode !== 'workflow') ? 'chat' : app.mode
  return `${appBaseURL}/${appMode}/${accessToken}`
}

export const getRedirection = (
  isCurrentWorkspaceEditor: boolean,
  app: App,
  redirectionFunc: (href: string) => void,
) => {
  if (!isCurrentWorkspaceEditor) {
    fetchAppDetail({ url: '/apps', id: app.id })
      .then((res) => {
        const appURL = buildDeploymentUrl(res)
        redirectionFunc(appURL)
      // New logic to build and redirect to the deployment URL
      // router.push(deploymentUrl);
      })
    // redirectionFunc(`/app/${app.id}/overview`)
  }
  else {
    if (app.mode === 'workflow' || app.mode === 'advanced-chat')
      redirectionFunc(`/app/${app.id}/workflow`)
    else
      redirectionFunc(`/app/${app.id}/configuration`)
  }
}
