---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_pak_2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_pak_2017
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_pak_2017
dataset_id: rdls_el-pak_wfp_integratedcontextanalysis_2017
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
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_pak_2017]'
details: null
exposure:
- asset_type:
    description: Population density distribution across Pakistan in 2015
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
    description: Land degradation extent and land cover classification 1992-2015
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: The ICA combines historical hazard occurrence data (floods, droughts,
    earthquakes, landslides 1905-2015) with multi-year food security trend analysis
    (2004-2017) and population density mapping to produce sub-national vulnerability
    classifications. Hazard layers were derived from observed historical events, while
    food insecurity vulnerability was assessed through consultations and trend analysis
    to identify areas where different programme strategies are appropriate for reducing
    food insecurity and climate shock risk.
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
- href: https://data.humdata.org/dataset/wfp_ica_pak_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population vulnerability and recurrence of food insecurity linked
      to flood hazard exposure
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
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population vulnerability and recurrence of food insecurity linked
      to drought hazard exposure
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2c8b469fc409464d9ada097541fcaed0/data
  format: PNG
  id: resource_706aa854
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Land Degradation, 1992-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the additional environmental
    hazards - landslides, Glacial Lake Outburst Flood (GLOF) and earthquakes - estimated
    during the Integrated Context Analysis (ICA) run in Pakistan in 2017. Data source:
    NDMA 1950-2015 (landslides and GLOF), NDMA 1905-2015 (earthquakes). The key indicators
    used for the analysis were 5-point scales of hazard levels ranging from very low
    to very high. It should be noted that these additional hazards represent aggravating
    factors that can provide further details to refine broad programmatic strategies,
    but are not to be considered as stand-alone maps. For the purpose of this analysis,
    only the high and very high hazards have been mapped on top of the ICA Areas (see
    the relative static maps for further details).'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/513e1f0658844cc6bad68e7b277298ff/data
  format: null
  id: resource_8cbb2ec1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Additional Hazards
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b3f7c9878ad344c5ab0ee6e8921ed961/data
  format: PNG
  id: resource_c8f61d47
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - GLOF Hazard, 1950-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the flood risk estimated during
    the Integrated Context Analysis (ICA) performed in Pakistan in 2017. The indicator
    used was the number of flood events recorded between 1950 and 2015 and the severity
    by which they were affected by the super-flood in 2010. Source: National Disaster
    Management Agency (NDMA) for Pakistan.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/951ac366904046ee854114183597c598/data
  format: null
  id: resource_fb488bff
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Flood Hazard, 1950-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the drought risk estimated during
    the Integrated Context Analysis (ICA) performed in Pakistan in 2017. Data source:
    National Drought Monitoring Centre of the Pakistan Meteorological Department (PMD),
    1951-2010. The key indicator used for the analysis was a drought hazard index
    based on SPI data.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5c56890c260348ad98f1849fd9e2a31f/data
  format: null
  id: resource_dc91d53f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Drought Hazard, 1951-2010
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization, in
    the Federally Administered Tribal Areas (FATA), resulting from the Integrated
    Context Analysis (ICA) run in Pakistan in 2017, showing areas of convergence between
    high levels of food insecurity and propensity to natural shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/764e57b0a3f74bce877a5f7c28358540/data
  format: null
  id: resource_3e035319
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, FATA, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d46acc160ea249d080b323701935e432/data
  format: PNG
  id: resource_3d5ef587
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Recurrence of Vulnerability to Food Insecurity, 2004-2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/086b0ce9b4514585910dc9c1c0345211/data
  format: PNG
  id: resource_67fb1ba5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Flood Hazard, 1950-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/9c65f322404d40a7b2765d214329d048/data
  format: PNG
  id: resource_d0910c64
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Earthquake Hazard, 1905-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/92fdf2e12543432a9dfda723fa9b159b/data
  format: PNG
  id: resource_04772040
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - ICA Categories
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c7bfc320aae84a4ab22bd02505fc78a5/data
  format: PNG
  id: resource_a969a43f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Two Most Dominant Land Cover Classes, 2009
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/38b5b734b9bb4598b9b56a96905ce29a/data
  format: PNG
  id: resource_32baba85
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - ICA Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/55765f5ae0424e9f8ecd7542e5148c1f/data
  format: PNG
  id: resource_f3dfc54b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Drought Hazard, 1951-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/0a18b3eedcc9464e81c332d5146015b1/data
  format: PNG
  id: resource_95ae97de
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Landslide Hazard, 1950-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/6426f5c2d3b2453da6682ac915a3ae72/data
  format: PNG
  id: resource_b523baeb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Programmatic Recommendations
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the final categorization resulting
    from the Integrated Context Analysis (ICA), run in Pakistan in 2017, showing areas
    of convergence between high recurrence of food insecurity and high propensity
    to natural shocks.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/b5675c4803fb4fe0b2621c522a3c4db6/data
  format: null
  id: resource_96965aa9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - ICA Categories & Areas
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c56e3805853d481cae84389e5ffe1b58/data
  format: PNG
  id: resource_1e498c9f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Combined Hazard (Floods and Drought)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Pakistan: Integrated Context Analysis (ICA), 2017 (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8d361c8b837c40a1872df3595cacf8fb/data
  format: PNG
  id: resource_94204a47
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Population Density, 2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: '''Integrated Context Analysis on Vulnerability to Food Insecurity
    and Natural Hazards'' (ICA) is a joint initiative by the United Nations World
    Food Programme (WFP) and the National Disaster Management Authority (NDMA) in
    close collaboration with the United Nations Food and Agriculture Organization
    (FAO) and relevant line departments, ministries and technical institutions of
    Pakistan. The study has been carried out under the overall leadership of NDMA
    from December 2016 to September 2017.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d9e9b46671d84d7abfdf6422a2e33d72/data
  format: null
  id: resource_4abd2032
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Integrated Context Analysis (ICA) On Vulnerability to Food Insecurity and
    Natural Hazards Pakistan, 2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer contains information about the reclassification of the natural
    shocks risk (floods and drought) into a single combined score according to the
    Integrated Context Analysis (ICA) performed in Pakistan in 2017.
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/32242f438b054b1cbd79f4a01489058b/data
  format: null
  id: resource_c7785521
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Combined Hazard (Floods and Droughts)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the risk of food insecurity
    according to the Integrated Context Analysis (ICA) performed in Pakistan in 2017.
    Given that no other food security outcome data was available at district level
    for the whole country, the analysis was carried out using poverty data as a proxy
    for vulnerability to food insecurity. Data source: UNDP, 2004/05 to 2005/06. The
    key indicator used for the analysis was the Multi-Dimensional Poverty Index (MPI),
    with the threshold set to 0.329 - average of all the district-level observations
    over 6 PSLM rounds. It should be noted that 33 districts in the country did not
    have MPI data available and are not covered by this specific analysis.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4917987c638d41338376bb9162f70591/data
  format: null
  id: resource_3a0a064d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Recurrence of Vulnerability to Food Insecurity, 2004-2014
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the land degradation phenomenon
    observed during the Integrated Context Analysis (ICA) run in Pakistan in 2017.
    Data source: ESA (300m resolution) 1992-2015, FAO (lithology), WorldClim (rainfall
    incidence), land cover (NASA MODIS) and slope length (NASA SRTM digital elevation
    model). The key indicators used for the analysis were the average ecological change
    and the percentage of surface prone to erosion. It should be noted that land degradation,
    according to the current ICA methodology, is not a stand-alone map but has to
    be considered as a lens that, overlaid on top of the ICA Areas, provide further
    information to refine broad programmatic strategies. The brown-green scheme has
    just been used for the layer preview because, for the purposes of this analysis,
    only negative values of ecological change and districts with a surface prone to
    erosion above 20% have been used for the final map (see ''ICA Pakistan, 2017 -
    Land Degradation 1992-2015'' static map for further details).'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/30223919559945a785fdd0942476a467/data
  format: null
  id: resource_1e02761f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, 2017 - Land Degradation, 1992-2015
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This layer contains information about the risk of food insecurity,
    in the Federally Administered Tribal Areas (FATA), according to the Integrated
    Context Analysis (ICA) performed in Pakistan in 2017. In absence of MPI data for
    FATA and considering existing circumstances and the importance of evidence based
    information, a different dataset has been used Data source: WFP In-depth Food
    Security and Livelihood Assessments 2014 & 2017, Multi-Cluster Humanitarian Needs
    Assessment 2016 The key indicator used for the analysis was the composite food
    insecurity rate developed under the Consolidated Approach to Reporting on Indicators
    of Food Security (CARI), with the threshold set to 38%.'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/1dc3db38e1cf4d70972162eb8e67e1f6/data
  format: null
  id: resource_d06492f5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ICA Pakistan, FATA, 2017 - Recurrence of Vulnerability to Food Insecurity,
    2014-2017
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pak_wfp_integratedcontextanalysis_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Pakistan: Integrated Context Analysis (ICA), 2017'
version: null
vulnerability: null
---
