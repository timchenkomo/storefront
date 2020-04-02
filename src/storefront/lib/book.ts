export interface Group {
  /** Unique ID of group of products. */
  slug: string;

  /** Title of a product. */
  title: string;

  /** Author of a product. */
  author: string;

  /** Description of a product. */
  description: string;

  /** List of a product varieties. */
  products: Product[]
}

export enum ProductType {
  Digital = 'digital',
  Audio = 'audio',
  Printed = 'printed'
}

export interface Product {
  /** Unique product ID. */
  slug: string;

  /** Type of a product variety. */
  type: ProductType;

  /** Price of a product */
  price: number;

  /** Name of variety */
  title: string;

  /** List of formats to download file */
  formats: string[];
  sample_formats: string[];

  series: string;
  year_published: number;
  publisher: string;
  group_slug: string;
}


export const EmptyGroup: Group = {
  slug: 'null', title: 'Empty book', author: 'No one',  description: '', products: []
}

export const EmptyProduct: Product = {
  slug: '',
  price: -1,
  type: ProductType.Digital,
  title: '',
  formats: [],
  sample_formats: [],
  series: '',
  year_published: 0,
  publisher: '',
  group_slug: ''
}

export function productType(t: string): string {
  if (t === 'digital') { return 'Эл. книга' }
  if (t === 'audio') { return 'Аудиокнига' }
  if (t === 'printed') { return 'Печатная' }
  return 'Книга'
}
