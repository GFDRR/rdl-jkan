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
dataset_id: rdls_exp-coclico_laucm
description: 'Coastal Local Administrative Units (LAUs) subdivide countries into small
  administrative regions (NUTS 3) counties, districts, or similar local government
  areas, helping organise coastal data for policy and planning. LAUs support local
  classifications of coastal areas and urbanization levels (e.g DEGURBA, FUA). Spatial
  coverage: EU economic territory. Sources: Administrative boundaries, regional statistics.
  Common usage: Policy planning, urban and coastal analysis. [Source: This metadata
  record was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
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
  description: 'Coastal Local Administrative Units (LAUs) subdivide countries into
    small administrative regions (NUTS 3) counties, districts, or similar local government
    areas, helping organise coastal data for policy and planning. LAUs support local
    classifications of coastal areas and urbanization levels (e.g DEGURBA, FUA). Spatial
    coverage: EU economic territory. Sources: Administrative boundaries, regional
    statistics. Common usage: Policy planning, urban and coastal analysis.'
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
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/LAU_CM/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/LAU_CM/collection.json
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
  title: 'STAC Collection: CoCliCo - Municipalities [LAU_CM]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2FLAU_CM.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Municipalities
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
  description: CoCliCo - Municipalities (Snapshot of the collection's STAC items exported
    to GeoParquet format.)
  download_url: gs://coclico-data-public/coclico/LAU_CM/LAU_2020_NUTS_2021_01M_3035_CM.parquet
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
slug: rdls_exp-coclico_laucm
spatial:
  bbox:
  - -81.12146941539005
  - -29.12357316038395
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
title: CoCliCo - Municipalities
version: null
vulnerability: null
---
