---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-binh-dinh-province-2722
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-binh-dinh-province-2722
dataset_id: rdls_hl-vnm_unosat_detectedsurfacewatersexte_20171114
description: 'This map illustrates the satellite-detected surface waters in Binh DinhNam
  Province, Vietnam, as observed from the Sentinel-1 image acquired on 10 November
  2017, following the landfall of tropical cyclone DAMREY-17 on 05 November 2017.
  The districts located in the coastal areas have been affected by the floods; especially
  the ones located in the southern coastal part of the province and more particularly
  Phu Cat, An Nhon, Tuy Phuoc and Qui Nhon districts. Around 17,000 ha of lands were
  identified as flooded within the province of Bihn Dihn. It represents an increase
  of ~140 % of the surface waters in the analyzed zone. In this analyzed area and
  according to the WorldPop data, more than 100,000 people are potentially exposed
  to flood waters. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-binh-dinh-province-2722]'
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-1 synthetic aperture radar imagery
    acquired on 10 November 2017, comparing it with pre-event imagery to detect changes
    in surface water extent. The analysis identified flooded areas across Binh Dinh
    Province following tropical cyclone DAMREY-17 landfall, quantifying approximately
    17,000 ha of inundated agricultural land across affected coastal districts.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-binh-dinh-province-2722
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural land inundation from coastal flooding, approximately
      17,000 ha identified as flooded
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
  description: Viet Nam - Satellite Detected Surface Waters Extent in Binh Dinh Province
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171106VNM/FL20171106VNM_gdb.zip
  format: Geodatabase
  id: resource_82bf43fb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171106VNM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Viet Nam - Satellite Detected Surface Waters Extent in Binh Dinh Province
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171106VNM/FL20171106VNM_shp.zip
  format: null
  id: resource_d4e75bfc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171106VNM_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vnm_unosat_detectedsurfacewatersexte_20171114
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-14'
temporal_resolution: null
title: Viet Nam - Satellite Detected Surface Waters Extent in Binh Dinh Province
version: null
vulnerability: null
---
