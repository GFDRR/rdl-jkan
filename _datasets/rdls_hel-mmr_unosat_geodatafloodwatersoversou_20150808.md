---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-southeast-bago-state-myanmar-august-08-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-southeast-bago-state-myanmar-august-08-2015
dataset_id: rdls_hel-mmr_unosat_geodatafloodwatersoversou_20150808
description: 'This map illustrates satellite-detected flood waters in the Southern
  region of Bago State in the areas of Nyaungiebin, Daik-U, Waw, Shwegyin and Kyauktaga
  townships of Myanmar as imaged by the Sentinel-1 satellite on 6 August 2015. Waters
  along the Sittang River have expanded and inundated lands on either sides of the
  river bank. Total surface covered with water in the analyzed area has increased
  from a pre-flood level of 3% to 20% during the flood period, and as of 6 August
  2015 a total of ~70,000 ha of lands were affected. Most of the affected lands south
  of Daik-U town seem to be mainly agricultural fields, many of which are of course
  frequently inundated at other times as well. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-southeast-bago-state-myanmar-august-08-2015]'
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
    description: Agricultural lands inundated by fluvial flooding in Bago State townships
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Sentinel-1 satellite imagery acquired on 6 August 2015 was analyzed
    by UNOSAT through visual comparison with pre-flood baseline imagery to detect
    and delineate flood water extent. Analysts identified notable changes in water
    surface coverage, quantifying the increase from 3% to 20% of the study area and
    mapping approximately 70,000 hectares of inundated agricultural lands across five
    townships in southern Bago State.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-southeast-bago-state-myanmar-august-08-2015
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct impact on agricultural lands from fluvial flooding, with approximately
      70,000 hectares affected
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
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
  description: Geodata of Flood Waters Over Southeast Bago State, Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR_shp.zip
  format: null
  id: resource_4a3abafc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Southeast Bago State, Myanmar (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20150703MMR/FL20150703MMR.gdb.zip
  format: null
  id: resource_060d7c12
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150703MMR.gdb.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mmr_unosat_geodatafloodwatersoversou_20150808
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-08-08'
temporal_resolution: null
title: Geodata of Flood Waters Over Southeast Bago State, Myanmar
version: null
vulnerability: null
---
