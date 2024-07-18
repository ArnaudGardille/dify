import { useStore as useAppStore } from '@/app/components/app/store'

export const getRedirection = (
  isCurrentWorkspaceEditor: boolean,
  app: any,
  redirectionFunc: (href: string) => void,
) => {
  if (!isCurrentWorkspaceEditor) {
    const appURL = `${app.mode}/${app.site.app_base_url}/${app.site.access_token}`

    redirectionFunc(appURL)
  }
  else {
    if (app.mode === 'workflow' || app.mode === 'advanced-chat')
      redirectionFunc(`/app/${app.id}/workflow`)
    else
      redirectionFunc(`/app/${app.id}/configuration`)
  }
}
