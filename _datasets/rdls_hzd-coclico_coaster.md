---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: University of East Anglia (UEA)
  url: https://research-portal.uea.ac.uk/en/
creator:
  affiliation: null
  email: null
  name: University of East Anglia (UEA)
  url: https://research-portal.uea.ac.uk/en/
dataset_id: rdls_hzd-coclico_coaster
description: 'Coastal Change Segments uses the historical shoreline change regime
  from the ''Coastal Typologies and Erosion for Risk'' (CoasTER) database which integrates
  existing information on erosion and other relevant coastal characteristics for Europe''s
  coastal floodplains. Spatial coverage: European coastlines. Sources: Remote sensing,
  historical shoreline data (1984-2024). Common usage: Coastal erosion monitoring,
  sediment transport studies, policy and spatial planning. More Info about the dataset:
  User Handbook. [Source: This metadata record was automatically extracted from the
  STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: Er:m/yr
      process: coastal_erosion
      trigger: null
      type: erosion
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: erosion
license: CC-BY-4.0
lineage:
  description: 'Coastal Change Segments uses the historical shoreline change regime
    from the ''Coastal Typologies and Erosion for Risk'' (CoasTER) database which
    integrates existing information on erosion and other relevant coastal characteristics
    for Europe''s coastal floodplains. Spatial coverage: European coastlines. Sources:
    Remote sensing, historical shoreline data (1984-2024). Common usage: Coastal erosion
    monitoring, sediment transport studies, policy and spatial planning. More Info
    about the dataset: User Handbook'
  sources:
  - id: source_1
    license: null
    name: University of East Anglia (UEA)
    risk_data_type:
    - hazard
    type: dataset
    url: https://research-portal.uea.ac.uk/en/
    used_in: hazard
  - id: source_2
    license: null
    name: Deltares
    risk_data_type:
    - hazard
    type: dataset
    url: https://deltares.nl
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: University of East Anglia (UEA)
  url: https://research-portal.uea.ac.uk/en/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: Hanson, S.E., Nicholls, R.J, Calkoen, F. R. Le Cozannet, G. and Luijendijk,
    A. P (2025, in review) 'A geospatial database of coastal characteristics for erosion
    assessment of Europe's coastal floodplains'
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/coaster/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/coaster/collection.json
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
  title: 'STAC Collection: CoCliCo - Coastal Change Segments [coaster]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fcoaster.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Coastal Change Segments
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
  description: CoCliCo - Coastal Change Segments (Snapshot of the collection's STAC
    items exported to GeoParquet format.)
  download_url: gs://coclico-data-public/coclico/items/coaster.parquet
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
- hazard
schema: rdls-10
slug: rdls_hzd-coclico_coaster
spatial:
  bbox:
  - -31.386545494931003
  - 32.457482285641014
  - 60.24216959014434
  - 67.12036364463012
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025'
  start: '2025'
temporal_resolution: null
title: CoCliCo - Coastal Change Segments
version: null
vulnerability: null
---
