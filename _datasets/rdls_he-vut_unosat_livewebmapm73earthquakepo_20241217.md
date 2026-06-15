---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-m-7-3-earthquake-port-vila-vanuatu
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-m-7-3-earthquake-port-vila-vanuatu
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-m-7-3-earthquake-port-vila-vanuatu
dataset_id: rdls_he-vut_unosat_livewebmapm73earthquakepo_20241217
description: 'UNOSAT code: EQ20241217VUT, GDACS ID: 1458084 This application provides
  geospatial information on ongoing satellite based-assessment related with the 7.3M
  magnitude earthquakes in Vanuatu of the 17 December 2024 Important note: The boundaries
  and names shown, and the designations used on this map do not imply official endorsement
  or acceptance by the United Nations. The United Nations Satellite Centre -UNOSAT
  is not responsible for the misuse or misrepresentation of the map.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-m-7-3-earthquake-port-vila-vanuatu]'
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
    description: Population exposure in Port-Vila affected by the earthquake
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
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from before
    and after the 7.3 magnitude earthquake on 17 December 2024 to identify notable
    changes and assess population exposure in Port-Vila. The resulting geospatial
    assessment integrates satellite-derived observations with population data to characterize
    earthquake impacts.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-web-map-m-7-3-earthquake-port-vila-vanuatu
  rel: source
loss:
  losses: []
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
  description: UNOSAT Live Web Map -M 7.3 Earthquake - Port-Vila, Vanuatu (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/4053/UNOSAT_A3_PopulationExposure_EQ20241217VUT.xlsx
  format: null
  id: resource_f309b8be
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_A3_PopulationExposure_EQ20241217VUT.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-vut_unosat_livewebmapm73earthquakepo_20241217
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-12-17'
temporal_resolution: null
title: UNOSAT Live Web Map -M 7.3 Earthquake - Port-Vila, Vanuatu
version: null
vulnerability: null
---
