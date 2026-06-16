---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Eurostat
  url: https://ec.europa.eu/eurostat/web/nuts/local-administrative-units
creator:
  affiliation: null
  email: null
  name: Eurostat
  url: https://ec.europa.eu/eurostat/web/nuts/local-administrative-units
dataset_id: rdls_exp-coclico_lau
description: 'The LAUs are a administrative to help ensure that data are readily available
  and policies can be implemented effectively using these units, a subdivision of
  the NUTS 3 regions covering the EU''s whole economic territory and appropriate for
  implementing local level typologies included in Tercet, namely the coastal area
  and the degree of urbanisation (DEGURBA) classification, including city and functional
  urban areas (FUA) definitions. [Source: This metadata record was automatically extracted
  from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure:
- asset_type:
    description: land use/land cover footprints
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: The LAUs are a administrative to help ensure that data are readily
    available and policies can be implemented effectively using these units, a subdivision
    of the NUTS 3 regions covering the EU's whole economic territory and appropriate
    for implementing local level typologies included in Tercet, namely the coastal
    area and the degree of urbanisation (DEGURBA) classification, including city and
    functional urban areas (FUA) definitions.
  sources:
  - id: source_1
    license: null
    name: Eurostat
    risk_data_type:
    - exposure
    type: dataset
    url: https://ec.europa.eu/eurostat/web/nuts/local-administrative-units
    used_in: exposure
  - id: source_2
    license: null
    name: Deltares
    risk_data_type:
    - exposure
    type: dataset
    url: https://deltares.nl
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Eurostat
  url: https://ec.europa.eu/eurostat/web/nuts/local-administrative-units
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: None.
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/LAU/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/LAU/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Local administrative units [LAU]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2FLAU.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Local administrative units
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Local administrative units (Snapshot of the collection's
    STAC items exported to GeoParquet format.)
  download_url: gs://coclico-data-public/coclico/LAU/LAU_2020_NUTS_2021_01M_3035.parquet
  format: null
  id: resource_geoparquetstacitems
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoParquet STAC items
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-coclico_lau
spatial:
  bbox:
  - -81.78251054209933
  - -29.857519696177313
  - 93.1752791130622
  - 37.855412297701754
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024'
  start: '2024'
temporal_resolution: null
title: CoCliCo - Local administrative units
version: null
vulnerability: null
---
