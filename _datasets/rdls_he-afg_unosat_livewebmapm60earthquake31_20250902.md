---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-m-6-0-afghanistan-earthquake-31-august-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-m-6-0-afghanistan-earthquake-31-august-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-m-6-0-afghanistan-earthquake-31-august-2025
dataset_id: rdls_he-afg_unosat_livewebmapm60earthquake31_20250902
description: 'UNOSAT code: EQ20250901AFG, GDACS ID: 1498339 This application provides
  geospatial information on ongoing satellite based-assessment related with the 6.0
  M magnitude earthquake in Afghanistan on the 31 August 2025 Important note: The
  boundaries and names shown, and the designations used on this map do not imply official
  end. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-m-6-0-afghanistan-earthquake-31-august-2025]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposure by earthquake intensity zones
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired before
    and after the 31 August 2025 earthquake to identify damage patterns and assess
    population exposure by earthquake intensity zones. The resulting geospatial dataset
    integrates satellite-derived hazard information with population distribution data
    to characterize exposure across affected areas.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-web-map-m-6-0-afghanistan-earthquake-31-august-2025
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
  description: UNOSAT Live web map -M 6.0 Afghanistan Earthquake (31 August 2025)
    (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4189/UNOSAT_PopulationExposure_by_IntensotyZones_EQ20250901AFG_Version%204.xlsx
  format: null
  id: resource_c0ed7a3e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_by_IntensotyZones_EQ20250901AFG_Version 4.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-afg_unosat_livewebmapm60earthquake31_20250902
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-09-02'
temporal_resolution: null
title: UNOSAT Live web map -M 6.0 Afghanistan Earthquake (31 August 2025)
version: null
vulnerability: null
---
