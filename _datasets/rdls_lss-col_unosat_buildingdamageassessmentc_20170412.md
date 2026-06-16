---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-the-city-of-mocoa-colombia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-the-city-of-mocoa-colombia
dataset_id: rdls_lss-col_unosat_buildingdamageassessmentc_20170412
description: 'Following a large mudflow that hit the city of Mocoa (Department of
  Putumayo, Colombia) on 31 March 2017 as a consequence of the heavy rains, the International
  Charter Space and Major Disasters has been activated upon the request of the National
  Unit for Disaster Risk Management (UNGRD) / Unidad Nacional para la Gestion del
  Riesgo de Desastres, IDEAM. In response to this emergency, UNITAR-UNOSAT has carried
  out satellite based damage analysis to assess (visible) building structural damage
  caused by mudflows. This map illustrates satellite-detected damaged structures including
  building damage density in Mocoa city and its surroundings. Analysis has been undertaken
  by using post satellite imagery acquired by Pleiades and Geoeye-1 satellites on
  the 7 and 10 April 2017 and pre satellite images acquired by Worldview-2 & 1 satellites
  on the 21 December 2016 and 26 December 2013. As result of UNOSAT satellite analysis,
  a total of 1,082 buildings were detected as damaged of which 736 observed as destroyed
  or washed out by mudflow and 346 observed as severely damaged. Due to the pronounced
  incident angle and cloud cover of the satellite images, UNITAR-UNOSAT has also used
  orthophotos collected by Corpoamazonia in order to validate satellite based analysis.
  Orthophotos and additional baseline data were provided by OSM Humanitarian Mapping
  Unit and UMAIC (Unidad de Manejo y Analisis de Informacion de Colombia) who is also
  providing information management coordination support for this event. Kindly note
  that the number of damaged structures could have been underestimated due to the
  parameters of the images. This analysis has not yet been validated in the field.
  Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/building-damage-assessment-in-the-city-of-mocoa-colombia]'
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    acquired before and after the 31 March 2017 mudflow event in Mocoa, Colombia.
    Notable changes in building structures were identified and classified by damage
    status and confidence level. The resulting geodatabase contains satellite-detected
    damaged building footprints with validation and confidence metadata.
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
- href: https://data.humdata.org/dataset/building-damage-assessment-in-the-city-of-mocoa-colombia
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building structural damage from mudflow event detected via
      satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: Colombia - Building Damage Assessment in the city of Mocoa (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL.gdb.zip
  format: Geodatabase
  id: resource_3ae21d18
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Building Damage Assessment in the city of Mocoa (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL_SHP.zip
  format: null
  id: resource_1b5716ba
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_unosat_buildingdamageassessmentc_20170412
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-12'
temporal_resolution: null
title: Colombia - Building Damage Assessment in the city of Mocoa
version: null
vulnerability: null
---
