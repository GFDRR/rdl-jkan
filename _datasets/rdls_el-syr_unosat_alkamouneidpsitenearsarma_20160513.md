---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-kamoune-idp-site-near-sarmada-idlib-governorate-syria-may-13-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-kamoune-idp-site-near-sarmada-idlib-governorate-syria-may-13-2016
dataset_id: rdls_el-syr_unosat_alkamouneidpsitenearsarma_20160513
description: 'This map illustrates satellite-detected areas of intact and destroyed
  structures at the Al-Kamoune IDP site, situated near the town of Sarmada in Idlib
  Governorate, Syria. Using 12 May 2016 and 16 April 2016 satellite imagery collected
  by the Deimos-2 and Pleiades satellites respectively, UNITAR-UNOSAT identified a
  total of 1,242 structures. Approximately 1,182 of these structures appeared to be
  intact and 60 destroyed on 12 May 2016, following an airstrike that hit the site
  on 05 May 2016. At least two different areas were affected, one of which was covered
  by sand or gravel as of 12 May 2016. Reconstruction appears to have started a few
  days prior to this. Due to lower resolution of the 12 May 2016 image there is a
  higher than usual level of uncertainty in this analysis. This is a preliminary analysis
  & has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-al-kamoune-idp-site-near-sarmada-idlib-governorate-syria-may-13-2016]'
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
    description: Shelter structures at Al-Kamoune IDP site classified by integrity
      status (intact vs. destroyed)
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (16 April
    2016 and 12 May 2016) from Pleiades and Deimos-2 sensors to detect structural
    damage at the Al-Kamoune IDP site following an airstrike on 05 May 2016. Visual
    interpretation identified 1,242 total structures with classification of intact
    (1,182) versus destroyed (60) status to assess direct impact on displaced population
    shelter infrastructure.
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
- href: https://data.humdata.org/dataset/geodata-of-al-kamoune-idp-site-near-sarmada-idlib-governorate-syria-may-13-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from airstrike event on 05 May 2016 at IDP
      site
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
  description: Syria - Al-Kamoune IDP Site Near Sarmada (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Al_Kamoune_20160416_shp.zip
  format: null
  id: resource_97963bec
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Kamoune_20160416_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Syria - Al-Kamoune IDP Site Near Sarmada (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Al_Kamoune_20160416.gdb.zip
  format: null
  id: resource_4823fcef
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Kamoune_20160416.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_alkamouneidpsitenearsarma_20160513
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-05-13'
temporal_resolution: null
title: Syria - Al-Kamoune IDP Site Near Sarmada
version: null
vulnerability: null
---
