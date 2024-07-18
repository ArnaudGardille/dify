import { useStore as useAppStore } from '@/app/components/app/store'

export const getRedirection = (
  isCurrentWorkspaceEditor: boolean,
  app: any,
  redirectionFunc: (href: string) => void,
) => {
  if (!isCurrentWorkspaceEditor) {
    const appBaseUrl = app.site?.app_base_url || "";
    const accessToken = app.site?.access_token || "";
    if (!appBaseUrl) {
      console.error("Error: Missing app base URL");
      // Optionally, redirect to an error page or display a message
      return;
    }
    if (!accessToken) {
      console.error("Error: Missing access token");
      // Optionally, redirect to an error page or display a message
      return;
    }
    
    const appURL = `${app.mode}/${appBaseUrl}/${accessToken}`;
    redirectionFunc(appURL);
  }
  else {
    if (app.mode === 'workflow' || app.mode === 'advanced-chat')
      redirectionFunc(`/app/${app.id}/workflow`)
    else
      redirectionFunc(`/app/${app.id}/configuration`)
  }
}
