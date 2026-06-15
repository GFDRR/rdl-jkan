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
dataset_id: rdls_hzd-coclico_shorelineprojectionsedito
description: 'Shoreline change projections under different climate scenarios (SSPs).
  Includes structured sample-wise accretion/erosion and sea level rise (SLR) projections
  with per-transect median and percentile summaries. [Source: This metadata record
  was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    erosion:
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
  event_sets_count: 1
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Shoreline change projections under different climate scenarios (SSPs).
    Includes structured sample-wise accretion/erosion and sea level rise (SLR) projections
    with per-transect median and percentile summaries.
  sources:
  - id: source_1
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
loss:
  losses: []
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
  doi: null
  id: ref_citation
  name: Calkoen et al., 2025. Present-day coastal erosion threatens buildings globally
    with sea-level rise increasing future risk.
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/shoreline-projections-edito/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/shoreline-projections-edito/collection.json
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
  title: 'STAC Collection: CoCliCo - Global Shoreline Change Projections [shoreline-projections-edito]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Shoreline change projections for global coastal transects, combining
    accretion/erosion trends and sea level rise impacts with spatial output in point
    format.
  download_url: az://items/shoreline-projections-edito.parquet
  format: null
  id: resource_data
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Shoreline Projections
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Global Shoreline Change Projections (Snapshot of the collection's
    STAC items exported to GeoParquet format.)
  download_url: https://coclico.blob.core.windows.net/items/shoreline-projections-edito.parquet
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
slug: rdls_hzd-coclico_shorelineprojectionsedito
spatial:
  bbox:
  - -179.84900256923657
  - -68.93437164540674
  - 179.8812171641805
  - 80.71599602776956
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '2030'
temporal_resolution: null
title: CoCliCo - Global Shoreline Change Projections
version: null
vulnerability: null
---
