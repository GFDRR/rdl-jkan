---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_cod_2018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_cod_2018
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_cod_2018
dataset_id: rdls_hel-cod_wfp_integratedcontextanalysis_2018
description: 'The ICA is a process of consultations supported by mapped-out data that
  produces a strategic plan describing where different combinations of programme themes
  are appropriate to achieve goals of reducing food insecurity and climate related
  shock risk. The ICA combines multi-year food security trends with natural shock
  risk data to highlight sub-national areas where different programme strategies make
  sense. Food security trend maps shows areas where safety nets can address regular
  food insecurity, and others where shocks make recovery more important. Climate-related
  natural shock risk maps show where DRR, preparedness and early warning efforts can
  complement food-security objectives. Atop this core foundation, mapped data on subjects
  including nutrition, gender, livelihoods and resilience can enrich theme-level strategic
  planning in which all pieces work together. The full group of ICA partners discuss
  these analytical results to arrive at strategic programmatic directions.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_cod_2018]'
details: null
exposure:
- asset_type:
    description: Population exposed to recurrent food insecurity and climate-related
      shocks
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
- asset_type:
    description: Agricultural areas subject to food insecurity trends and shock risk
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
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
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: ODbL-1.0/
lineage:
  description: The ICA integrates multi-year food security trend data (EFSA 2012-2018)
    with climate-related natural shock risk assessments to identify sub-national areas
    where food insecurity is recurrent or shock-driven, enabling targeted programme
    strategy recommendations for reducing food insecurity and climate shock vulnerability.
  sources:
  - id: source_1
    license: null
    name: World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_cod_2018
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity impact from drought and climate-related shocks on
      agricultural populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  description: "This layer contains information about the recurrence of food insecurity\
    \ - by second-level administrative area - resulting from the Emergency Food Security\
    \ Assessments (EFSAs) used to integrate the food security analysis performed for\
    \ the Integrated Context Analysis (ICA) run in Democratic Republic of Congo in\
    \ 2017. The emergency assessments were performed in the hot-spot province of Sud-Kivu.\
    \ Data source: Emergency Food Security Assessment (EFSA), 2012-2018. The main\
    \ indicator used for the analysis was the recurrence of food insecurity conditions,\
    \ using a threshold set to 20%. Cette couche contient les donn\xE9es d'une analyse\
    \ de tendance de la s\xE9curit\xE9 alimentaire - par unit\xE9 administrative de\
    \ deuxi\xE8me niveau - utilis\xE9e au fin de int\xE9grer l'analyse employ\xE9\
    e pendant l'Analyse Integr\xE9e de Contexte (AIC) ex\xE9cut\xE9 en R\xE9publique\
    \ D\xE9mocratique du Congo en 2017. L'analyse additionelle a \xE9t\xE9 execut\xE9\
    e dans trois dans la province de Sud-Kivu. Source des donn\xE9es: Emergency Food\
    \ Security Assessment (EFSA), 2012-2018. L'indicateur principale utilis\xE9 pour\
    \ l'analyse \xE9tait la r\xE9currence d'ins\xE9curit\xE9 alimentaire, avec un\
    \ seuil fix\xE9 \xE0 20%."
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1bcfd972bf264f538b324275e1dbb47f/data
  format: null
  id: resource_e31cb251
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Democratic Republic of Congo, 2017 - Recurrence of Food Insecurity, EFSA
    2012-2018
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cod_wfp_integratedcontextanalysis_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: 'Democratic Republic of the Congo: Integrated Context Analysis (ICA), 2018'
version: null
vulnerability: null
---
