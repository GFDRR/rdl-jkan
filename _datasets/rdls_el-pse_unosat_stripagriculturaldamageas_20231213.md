---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-december-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-december-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-december-2023
dataset_id: rdls_el-pse_unosat_stripagriculturaldamageas_20231213
description: 'UNOSAT code: CE20231007PSE This map illustrates satellite-detected changes
  in agricultural areas of the Gaza Strip resulting from the decline in the health
  and density of crops due to the ongoing conflict. UNOSAT conducted an analysis utilising
  satellite imagery collected by the Sentinel-2 satellite between December 2017 and
  2023, performing a Normalised Difference Vegetation Index (NDVI) analysis as well
  as a multi-temporal classification to identify notable changes taking place in agricultural
  areas during that timeframe. The methodology evaluated the damage as a substantial
  decline in the health and density of crops in December 2023, in comparison to the
  preceding six seasons spanning from 2017 to 2022. The decline in the health and
  density of the crops can be observed due to the impact of activities such as razing,
  heavy vehicle activity, bombing, shelling, and other conflict-related dynamics.
  The analysis takes into account the damage that affects both active crop fields,
  fallow lands, and a multitude of household gardens. UNOSAT analysis shows that the
  agricultural extent in the Gaza Strip is estimated to be 185 sq. km, accounting
  for approximately 50% of the total area of Gaza. Compared to the average of the
  previous 6 years, approximately 18% of the arable land in the Gaza Strip has exhibited
  a significant decline in health and density in November 2023. Furthermore, the analysis
  shows that there has been a significant increase in damage to the arable land in
  the North Gaza Governorate, with around 39% of its land being impacted. Additionally,
  there has been an increase in agricultural land damage in the Gaza Governorate,
  rising from 17% to 27% between imagery collected on November 2023 and December 2023.
  This is a preliminary analysis and has not yet been validated in the field.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-december-2023]'
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
    description: Agricultural land areas in Gaza Strip classified by crop health and
      vegetation density changes
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-2 satellite imagery spanning December
    2017 to December 2023, applying Normalised Difference Vegetation Index (NDVI)
    analysis and multi-temporal classification to detect changes in agricultural vegetation
    health and density. Satellite-detected changes in crop condition were mapped to
    quantify agricultural damage resulting from the ongoing conflict.
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
- href: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-assessment-december-2023
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural damage assessed through vegetation index decline
      in Gaza Strip agricultural areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Palestine - UNOSAT Gaza Strip Agricultural Damage Assessment - December
    2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3772/UNOSAT_GazaStrip_Agriculture_DA_GDB.zip
  format: Geodatabase
  id: resource_a3bfeb6c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_GazaStrip_Agriculture_DA_GDB.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_stripagriculturaldamageas_20231213
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-12-13'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Agricultural Damage Assessment - December 2023
version: null
vulnerability: null
---
