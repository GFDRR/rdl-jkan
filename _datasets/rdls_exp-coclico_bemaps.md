---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: BRGM
  url: www.brgm.fr
creator:
  affiliation: null
  email: null
  name: BRGM
  url: www.brgm.fr
dataset_id: rdls_exp-coclico_bemaps
description: 'Building Exposure identifies the vulnerability of buildings in low elevation
  coastal zones (LECZ) to coastal flooding under various climate change scenarios.
  Spatial coverage: European coastal areas. Sources: OpenStreetMap building data,
  CoCliCo inundation maps, regional sea level projections, and extreme weather data.
  Common usage: Supports building exposure assessments, informs coastal resilience
  and adaptation planning, engages stakeholders with accessible data, and helps prioritize
  investments and strategic land-use decisions. More Info about the dataset: User
  Handbook. Variants in the source dataset - defense level: HIGH_DEFENDED_MAPS (High
  Defended), LOW_DEFENDED_MAPS (Low Defended), UNDEFENDED_MAPS (No Defense) - Policy-based
  coastal protection standards at the province level (NUTS2). High (low) defended:
  maximum (minimum) level of policy-based protection, if information is available.
  No defense: without protection (beyond what may be included in the DEM); return
  period: static (No Return Period), 1 (1 year), 100 (100 years), 1000 (1000 years)
  - Frequency at which an extreme event of total water level (related to storms) is
  expected to occur on average; scenarios: None (No Scenario), SSP126 (SSP1-2.6),
  SSP245 (SSP2-4.5), SSP585 (SSP5-8.5) - Climate scenarios based on IPCC''s Shared
  Socioeconomic Pathways (SSPs). High-end (if applicable) refers to P83 of SSP5-8.5,
  taking into account low-confidence processes. Other scenarios use the P50; time:
  2010, 2030, 2050, 2100 - Time slice applied to the data. Either present-day (2010)
  or future state representing medium (2030 till 2050) and long term (2050 till 2100)
  outlook. Metric unit: data values presented as % (source: deltares:units); RDLS
  exposure metric kept at category-default count/count. [Source: This metadata record
  was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure:
- asset_type:
    description: building footprints
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: 'Building Exposure identifies the vulnerability of buildings in low
    elevation coastal zones (LECZ) to coastal flooding under various climate change
    scenarios. Spatial coverage: European coastal areas. Sources: OpenStreetMap building
    data, CoCliCo inundation maps, regional sea level projections, and extreme weather
    data. Common usage: Supports building exposure assessments, informs coastal resilience
    and adaptation planning, engages stakeholders with accessible data, and helps
    prioritize investments and strategic land-use decisions. More Info about the dataset:
    User Handbook'
  sources:
  - id: source_1
    license: null
    name: BRGM
    risk_data_type:
    - exposure
    type: dataset
    url: www.brgm.fr
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
  name: BRGM
  url: www.brgm.fr
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: In preparation
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/be_maps/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/be_maps/collection.json
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
  title: 'STAC Collection: CoCliCo - Building Exposure [be_maps]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fbe_maps.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Building Exposure
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
  description: CoCliCo - Building Exposure (Snapshot of the collection's STAC items
    exported to GeoParquet format.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/be_stats/be_stats.parquet
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
slug: rdls_exp-coclico_bemaps
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
  end: '2010'
  start: '2010'
temporal_resolution: null
title: CoCliCo - Building Exposure
version: null
vulnerability: null
---
