---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20250708
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250708
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250708
dataset_id: rdls_hzd-phl_philsa_floodingjuly082025_20250708
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 08, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20250708]'
details: This dataset has not been validated using ground-truth data.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Satellite synthetic aperture radar (SAR) imagery from Sentinel-1 was
    processed to detect and map flood extent across the Philippines following typhoon
    impacts on July 8, 2025. The processing pipeline involved image classification
    to distinguish inundated areas from non-inundated areas, with results delivered
    as both raster (PNG) and vector (shapefile) formats for spatial analysis and impact
    tracking.
  sources:
  - id: source_1
    license: null
    name: Philippine Space Agency
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-flood-20250708
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 08, 2025 (Flooding extents on July
    08, 2025 at 05:32 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/962db92c-5735-4a9f-bce5-0f695a113b97/resource/6798fac1-70d1-4c8c-a2b1-f0ebd1832bcf/download/20250708_0532_fld_s1_maps.zip
  format: PNG
  id: resource_6798fac1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250708_0532_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 08, 2025 (Flooding extents on July
    08, 2025 at 05:32 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/962db92c-5735-4a9f-bce5-0f695a113b97/resource/59869d21-a668-434c-8ab2-092ee3337037/download/20250708_0532_fld_s1_shp.zip
  format: null
  id: resource_59869d21
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250708_0532_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingjuly082025_20250708
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-08'
temporal_resolution: null
title: Flooding in the Philippines on July 08, 2025
version: null
vulnerability: null
---
