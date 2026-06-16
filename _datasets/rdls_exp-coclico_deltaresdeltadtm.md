---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
dataset_id: rdls_exp-coclico_deltaresdeltadtm
description: 'A global coastal digital terrain model, based on CopernicusDEM, ESA
  WorldCover, ICESat-2 and GEDI data. For more information, see Pronk et al. (2024)
  DeltaDTM: A global coastal digital terrain model. [Source: This metadata record
  was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
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
  description: 'A global coastal digital terrain model, based on CopernicusDEM, ESA
    WorldCover, ICESat-2 and GEDI data. For more information, see Pronk et al. (2024)
    DeltaDTM: A global coastal digital terrain model.'
  sources:
  - id: source_1
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
  name: Deltares
  url: https://deltares.nl
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-024-03091-9
  id: ref_pub_1
  name: 'Pronk, Maarten, Aljosja Hooijer, Dirk Eilander, Arjen Haag, Tjalling de Jong,
    Michalis Vousdoukas, Ronald Vernimmen, Hugo Ledoux, and Marieke Eleveld. 2024.
    ''DeltaDTM: A Global Coastal Digital Terrain Model.'' Scientific Data 11 (1):
    273. https://doi.org/10.1038/s41597-024-03091-9.'
  url: https://doi.org/10.1038/s41597-024-03091-9
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/deltares-delta-dtm/collection.json
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
  title: 'STAC Collection: CoCliCo - DeltaDTM: A global coastal digital terrain model
    [deltares-delta-dtm]'
- access_url: https://coclico.blob.core.windows.net/assets/thumbnails/deltares-delta-dtm-thumbnail.jpeg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'CoCliCo - DeltaDTM: A global coastal digital terrain model'
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/jpeg
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
  description: 'CoCliCo - DeltaDTM: A global coastal digital terrain model (Snapshot
    of the collection''s STAC items exported to GeoParquet format.)'
  download_url: az://items/deltares-delta-dtm.parquet
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
slug: rdls_exp-coclico_deltaresdeltadtm
spatial:
  bbox:
  - -180.0
  - -68.9998611111111
  - 180.0
  - 84.00013888888888
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023'
  start: '2023'
temporal_resolution: null
title: 'CoCliCo - DeltaDTM: A global coastal digital terrain model'
version: null
vulnerability: null
---
