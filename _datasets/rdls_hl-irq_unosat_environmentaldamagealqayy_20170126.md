---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq
dataset_id: rdls_hl-irq_unosat_environmentaldamagealqayy_20170126
description: 'This map illustrates satellite-detected fires and environmental damage
  at and around Al Qayyarah, approximately 60 Km south of Mosul, Iraq. The main frame
  shows fires and the oil spill as seen in imagery collected between 23 December 2016
  and 24 January 2017. Marked in blue are fires that were detected in 23 December
  2016 but appear inactive as of 24 January 2017. Insets on the left show the oil
  spill north of Al Qayyarah, detected with both radar and optical imagery from multiple
  dates. As seen in the imagery, the oil spill is very close to one of the streams
  which is incidentally a tributary to the Tigris River; therefore, it is possible
  that oil is spilling to the river. The spectral signature from thermal imagery also
  suggest that areas of the oil spill are on fire. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq]'
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
  event_sets_by_hazard_type:
    wildfire:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FWI:-
        process: wildfire_smoke
        trigger: null
        type: wildfire
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (optical
    and radar) collected between December 2016 and January 2017 to detect and map
    active/inactive oil fires and oil spill extent near Al Qayyarah. Fire frequency
    and status were classified through visual interpretation and change detection
    analysis.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/environmental-damage-in-al-qayyarah-iraq
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Environmental damage from oil fires and oil spill contamination detected
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
  description: Iraq - Environmental damage in Al Qayyarah (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah_oil_fires.gdb.zip
  format: Geodatabase
  id: resource_30c82ce9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah_oil_fires.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Environmental damage in Al Qayyarah (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah_oil_fires.shp.zip
  format: null
  id: resource_1dc8db53
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah_oil_fires.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Environmental damage in Al Qayyarah (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah.gdb.zip
  format: Geodatabase
  id: resource_16658882
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Environmental damage in Al Qayyarah (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah_shp.zip
  format: null
  id: resource_b53e538e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Environmental damage in Al Qayyarah (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah_20161121_oil_fires.gdb.zip
  format: Geodatabase
  id: resource_7adb707c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah_20161121_oil_fires.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Environmental damage in Al Qayyarah (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Al_Qayyarah_20161121_oil_fires.shp.zip
  format: null
  id: resource_8e558c65
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Al_Qayyarah_20161121_oil_fires.shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-irq_unosat_environmentaldamagealqayy_20170126
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-01-26'
temporal_resolution: null
title: Iraq - Environmental damage in Al Qayyarah
version: null
vulnerability: null
---
