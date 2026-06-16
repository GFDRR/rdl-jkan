---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-democratic-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-democratic-
dataset_id: rdls_hel-lao_unosat_detectedwaterextentoversa_20180726
description: 'This map illustrates the satellite-detected surface waters extent in
  Sanamxay district, Attapeu province, as observed from the Radarsat-2 radar image
  acquired on 24 July 2018. The previous day, the Xe-Namnoy dam collapsed, inducing
  flash floods along the Vang Ngao river and affecting several villages located 50
  km downstream. Within the analysed area 14,692 ha of surface waters were detected
  after the heavy rains that happened on 22 July and as well the collapse of the dam.
  Several villages and surrounding agricultural fields seems to be inundated. The
  villages of Ban Hinlat, Ban Thaseangchan, Ban Mai and Ban Samong-tai seems to be
  the most affected ones. It is likely that flood waters have been systematically
  underestimated along highly vegetated areas, along the main riverbanks and within
  built-up urban areas because of the special characteristics of the used satellite
  data. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-democratic-]'
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
    description: Agricultural fields inundated by fluvial flooding in Sanamxay District
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Village settlements and structures affected by inundation in the
      study area
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Radarsat-2 radar satellite imagery acquired on 24 July 2018 was analyzed
    by UNOSAT to detect surface water extent in Sanamxay District following the 23
    July 2018 Xe-Namnoy dam collapse. Satellite-based change detection compared pre-
    and post-event imagery to identify inundated areas, resulting in a vector polygon
    dataset of 14,692 ha of detected surface waters affecting villages and agricultural
    fields downstream.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-democratic-
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct inundation of agricultural fields from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct inundation of village settlements from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
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
  description: Satellite detected water extent over Sanamxay District, Attapeu Province,
    Lao People Democratic Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LA/FL20180723LAO/FL20180723LAO_shp.zip
  format: null
  id: resource_1378802b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180723LAO_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lao_unosat_detectedwaterextentoversa_20180726
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-26'
temporal_resolution: null
title: Satellite detected water extent over Sanamxay District, Attapeu Province, Lao
  People Democratic Republic
version: null
vulnerability: null
---
