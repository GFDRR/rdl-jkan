---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-m-7-7-sagaing-earthquake-in-myanmar-thailand
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-m-7-7-sagaing-earthquake-in-myanmar-thailand
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-m-7-7-sagaing-earthquake-in-myanmar-thailand
dataset_id: rdls_hl-mmrtha_unosat_livewebmapm77sagaingearth_20250512
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This application provides
  geospatial information on ongoing satellite based-assessment related with the 7.7M
  magnitude Saigaing earthquake in Myanmar & Thailand on the 28 March 2025. Important
  note: The boundaries and names shown, and the designations used on this map do not
  imply official endorsement or acceptance by the United Nations. The United Nations
  Satellite Centre -UNOSAT is not responsible for the misuse or misrepresentation
  of the map.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-live-web-map-m-7-7-sagaing-earthquake-in-myanmar-thailand]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    to identify notable changes and damage patterns resulting from the 7.7 magnitude
    Sagaing earthquake. Damage assessments were conducted through visual interpretation
    of satellite data, with results compiled into geospatial datasets (geodatabase
    and shapefile formats) containing settlement-level damage classifications and
    confidence metrics.
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
- href: https://data.humdata.org/dataset/unosat-live-web-map-m-7-7-sagaing-earthquake-in-myanmar-thailand
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from satellite imagery analysis
      of the Sagaing earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
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
  description: UNOSAT Live Web Map - M 7.7 Sagaing Earthquake in Myanmar & Thailand
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4136/GDB.zip
  format: Geodatabase
  id: resource_266adc65
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Live Web Map - M 7.7 Sagaing Earthquake in Myanmar & Thailand
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4136/SHP.zip
  format: null
  id: resource_9c893ac5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmrtha_unosat_livewebmapm77sagaingearth_20250512
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  - THA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-05-12'
temporal_resolution: null
title: UNOSAT Live Web Map - M 7.7 Sagaing Earthquake in Myanmar & Thailand
version: null
vulnerability: null
---
