---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
  url: www.ivm.nl
creator:
  affiliation: null
  email: null
  name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
  url: www.ivm.nl
dataset_id: rdls_exp-coclico_ceedmaps
description: 'Critical infrastructure represents EU-wide high-resolution object-based
  maps of economic assets and infrastructure systems in coastal flood-prone areas.
  Grey polygons represent buildings of any kind, blue lines indicate line elements
  like roads, railways or powerlines and red dots show objects related to for instance
  power or telecom. Spatial coverage: Coastal LAU (municipality level) Sources: Satellite
  imagery and opensource databases (OpenStreetMap among others) Common usage: Supports
  building exposure assessments, informs coastal resilience and adaptation planning,
  engages stakeholders with accessible data, and helps prioritize investments and
  strategic land-use decisions. More Info about the dataset: User Handbook. [Source:
  This metadata record was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure:
- asset_type:
    description: infrastructure footprints
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: 'Critical infrastructure represents EU-wide high-resolution object-based
    maps of economic assets and infrastructure systems in coastal flood-prone areas.
    Grey polygons represent buildings of any kind, blue lines indicate line elements
    like roads, railways or powerlines and red dots show objects related to for instance
    power or telecom. Spatial coverage: Coastal LAU (municipality level) Sources:
    Satellite imagery and opensource databases (OpenStreetMap among others) Common
    usage: Supports building exposure assessments, informs coastal resilience and
    adaptation planning, engages stakeholders with accessible data, and helps prioritize
    investments and strategic land-use decisions. More Info about the dataset: User
    Handbook'
  sources:
  - id: source_1
    license: null
    name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
    risk_data_type:
    - exposure
    type: dataset
    url: www.ivm.nl
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
  name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
  url: www.ivm.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/ceed_maps/collection.json
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
  title: 'STAC Collection: CoCliCo - Critical Infrastructure [ceed_maps]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/ceed_maps.jpeg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Critical Infrastructure
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
  description: CoCliCo - Critical Infrastructure (Snapshot of the collection's STAC
    items exported to GeoParquet format.)
  download_url: gs://coclico-data-public/coclico/items/ceed_maps.parquet
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
slug: rdls_exp-coclico_ceedmaps
spatial:
  bbox:
  - -10.677069663150457
  - 34.541584997191165
  - 34.53596939451993
  - 70.12228553984926
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '2021'
temporal_resolution: null
title: CoCliCo - Critical Infrastructure
version: null
vulnerability: null
---
