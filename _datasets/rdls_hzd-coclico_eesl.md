---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
dataset_id: rdls_hzd-coclico_eesl
description: 'Extreme Sea Level combines tidal variations, storm surges, and long-term
  sea level rise to estimate high water levels. Indicators: Return periods, extreme-value
  analysis, percentile-based sea levels. Sources: Observational records, climate models,
  Copernicus Marine Service. Common usage: Coastal flood risk assessment, infrastructure
  design, emergency planning. More Info about the dataset: User Handbook. Variants
  in the source dataset - scenarios: RCP45 (RCP 4.5), RCP85 (RCP 8.5) - Climate scenarios
  based on IPCC''s Shared Socioeconomic Pathways (SSPs). High-end (if applicable)
  refers to P83 of SSP5-8.5, taking into account low-confidence processes. Other scenarios
  use the P50; rp: 5.0 (5 years), 10.0 (10 years), 20.0 (20 years), 50.0 (50 years),
  100.0 (100 years), 200.0 (200 years), 500.0 (500 years), 1000.0 (1000 years) - Frequency
  at which an extreme event of total water level (related to storms) is expected to
  occur on average; time: 1995-01-01T00:00:00Z, 2100-01-01T00:00:00Z - decade window;
  lon: -10.384861694088558, 41.71565682677875 - longitude; lat: 34.5687629160239,
  71.15531044927368 - latitude; ensemble: min, mean, max. [Source: This metadata record
  was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 8
    events:
    - calculation_method: simulated
      description: 'Return period 5 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_5
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5.0
    - calculation_method: simulated
      description: 'Return period 10 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_10
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 10.0
    - calculation_method: simulated
      description: 'Return period 20 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_20
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20.0
    - calculation_method: simulated
      description: 'Return period 50 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_50
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 50.0
    - calculation_method: simulated
      description: 'Return period 100 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_100
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100.0
    - calculation_method: simulated
      description: 'Return period 200 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_200
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 200.0
    - calculation_method: simulated
      description: 'Return period 500 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_500
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 500.0
    - calculation_method: simulated
      description: 'Return period 1000 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_1000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 1000.0
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://example.org/license/unknown
lineage:
  description: 'Extreme Sea Level combines tidal variations, storm surges, and long-term
    sea level rise to estimate high water levels. Indicators: Return periods, extreme-value
    analysis, percentile-based sea levels. Sources: Observational records, climate
    models, Copernicus Marine Service. Common usage: Coastal flood risk assessment,
    infrastructure design, emergency planning. More Info about the dataset: User Handbook'
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - hazard
    type: dataset
    url: https://www.deltares.nl
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/eesl/collection.json
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
  title: 'STAC Collection: CoCliCo - Extreme Sea Level [eesl]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Extreme Sea Level (The root of the Extreme Sea Levels zarr
    dataset on public Google Cloud Storage.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/europe_extreme_sea_level.zarr
  format: null
  id: resource_data
  media_type: application/vnd.zarr
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Extreme Sea Levels zarr root
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/eesl.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Extreme Sea Level
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
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-coclico_eesl
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: CoCliCo - Extreme Sea Level
version: null
vulnerability: null
---
