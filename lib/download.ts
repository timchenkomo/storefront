import { Group, Product } from '@/lib/book.ts'

export function getSampleUrl(group: Group, filename: string) {
  return '/api/download/' + group.slug + '/sample_' + filename;
}

export function getProductUrl(product: Product, filename: string) {
  return '/api/download/' + product.slug + '/' + filename
}
