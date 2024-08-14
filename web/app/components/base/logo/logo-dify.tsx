'use client'
import type { FC } from 'react'
import classNames from '@/utils/classnames'
import { useSelector } from '@/context/app-context'

type LogoDifyProps = {
  className?: string
}

const LogoDify: FC<LogoDifyProps> = ({
  className,
}) => {
  const { theme } = useSelector((s) => {
    return {
      theme: s.theme,
    }
  })

  const src = theme === 'light' ? '/logo/logo-dify.png' : `/logo/logo-dify-${theme}.png`
  return (
    <img
      src={src}
      className={classNames('block w-auto h-10', className)}
      alt='logo'
    />
  )
}

export default LogoDify
