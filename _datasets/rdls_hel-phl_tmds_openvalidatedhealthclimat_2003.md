---
attributions:
- entity:
    affiliation: null
    email: null
    name: Department of Health (DOH)
    url: https://data.humdata.org/dataset/project-cchain
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Philippine Statistics Authority (PSA)
    url: https://data.humdata.org/dataset/project-cchain
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Project NOAH
    url: https://data.humdata.org/dataset/project-cchain
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERA5 and MERRA
    url: https://data.humdata.org/dataset/project-cchain
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Google Open Buildings
    url: https://data.humdata.org/dataset/project-cchain
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap (OSM)
    url: https://data.humdata.org/dataset/project-cchain
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Ookla and Nightlights
    url: https://data.humdata.org/dataset/project-cchain
  id: attribution_7
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Thinking Machines Data Science
  url: https://data.humdata.org/dataset/project-cchain
creator:
  affiliation: null
  email: null
  name: Thinking Machines Data Science
  url: https://data.humdata.org/dataset/project-cchain
dataset_id: rdls_hel-phl_tmds_openvalidatedhealthclimat_2003
description: 'The Project Climate Change, Health, and Artificial Intelligence (Project
  CCHAIN) dataset is a validated, open-sourced linked dataset containing 20 years
  (2003-2022) of climate, environmental, socioeconomic, and health dimensions at the
  barangay (village) level across twelve Philippine cities (Dagupan, Palayan, Navotas,
  Mandaluyong, Muntinlupa, Legazpi, Iloilo, Mandaue, Tacloban, Zamboanga, Cagayan
  de Oro, Davao). The full documentation can be accessed here . The tables are designed
  in a way that users can choose variables that are most relevant to their focus city
  and use case, and link these variables to form a single dataset by merging using
  standard geography codes and calendar dates. This can be done using the provided
  linking notebook , or offline using the user''s own code. Here are some tips on
  how make most use of this dataset: Focus on one location. Starting with a detailed
  analysis of one location allows for a better understanding of the local dynamics,
  which may differ across locations. Choose one health data source. Pick one of either
  a central or local data source. Using two different data health sources is not advised
  because it will lead to double/overcounting of disease cases. Do not use all variables
  at once- do a literature review first to identify possible key variables . to identify
  possible key variables. More often than not, using all variables is not necessary
  and may even yield subpar results. Check data availability on your focus location
  and make sure they fit the requirements of your study. This dataset also includes
  household surveys tables (see schema here and here ) done on partner informal settlement
  communities in the cities of Muntinlupa, Davao, Iloilo, and Mandaue and administered
  on various dates up to 2024. Due to the sensitive nature of surveys and the vulnerability
  of the subjects involved, requests for access must be submitted for review and approval
  by the Philippine Action for Community-Led Shelter Initiatives, Inc. (PACSII). To
  submit a request, please use this form .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/project-cchain]'
details: Kindly access the [full documentation](https://thinkingmachines.github.io/project-cchain)
  for more details. The dataset is under CC By 4.0 license, with one exception, the
  [tm_open_buildings](https://dbdocs.io/lacuna-fund-project-team/Project-CCHAIN?table=tm_open_buildings)
  table, follows the [**Open Database License (ODbL)**](http://opendatacommons.org/licenses/odbl/1.0/)
  as directed by its source, OpenStreetMap.
exposure:
- asset_type:
    description: Building footprints and counts from Google Open Buildings dataset
      across twelve Philippine cities
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
- asset_type:
    description: Health facilities, water bodies, sanitation infrastructure, and amenities
      from OpenStreetMap and DOH geoportal
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
- asset_type:
    description: Population distribution and accessibility to health facilities via
      isochrone analysis
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    extreme_temperature:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AirTemp:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The dataset integrates 20 years (2003-2022) of climate, environmental,
    health, and socioeconomic data from multiple national government agencies (DOH,
    PSA, Project NOAH) and freely-available geospatial sources (ERA5, MERRA, Google,
    ESA, OpenStreetMap, Mapbox) at barangay level across twelve Philippine cities.
    All source data underwent vetting and validation processes before integration
    into linked tables enabling multi-dimensional analysis of climate-health relationships.
  sources:
  - id: source_1
    license: null
    name: Department of Health (DOH)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Philippine Statistics Authority (PSA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Project NOAH
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: ERA5 and MERRA
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Google Open Buildings
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_6
    license: null
    name: OpenStreetMap (OSM)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_7
    license: null
    name: Ookla and Nightlights
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/project-cchain
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Disease cases and deaths from temperature-sensitive illnesses recorded
      through PIDSR, FHSIS, and PSA health surveillance systems
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
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
  description: Total disease cases (morbidity) reported in Department of Health- Philippine
    Integrated Disease Surveillance and Response (DOH-PISDR) framework. Data is in
    city-weekly resolution. This data, requested by Epimetrics from their respective
    data owners, is governed by Data Use Agreements that allows for public use for
    climate and health applications.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/b93c1427-797a-40a4-b99e-872e152d1c86/download/disease_pidsr_totals.csv
  format: null
  id: resource_b93c1427
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disease_pidsr_totals.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Total disease deaths (mortality) and cases (morbidity) reported by
    the Department of Health- Field Health Services Information System. Data is in
    city-monthly resolution. This data, requested by Epimetrics from their respective
    data owners, is governed by Data Use Agreements that allows for public use for
    climate and health applications.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/07c85dbe-b542-44f9-aeef-34f72d877f8f/download/disease_fhsis_totals.csv
  format: null
  id: resource_07c85dbe
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disease_fhsis_totals.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Total disease-related deaths (mortality) recorded by the Philippine
    Statistical Authority (PSA) Vital Health Statistics division. Data is in city-weekly
    resolution. This data, requested by Epimetrics from their respective data owners,
    is governed by Data Use Agreements that allows for public use for climate and
    health applications.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/2a56f8ad-463b-4b0e-ad76-a7df610313d7/download/disease_psa_totals.csv
  format: null
  id: resource_2a56f8ad
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disease_psa_totals.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Baranggay-level age and sex-disaggregated disease deaths (mortality)
    and cases (morbidity) from reports submitted by the LGU to DOH-Field Health Services
    Information System (DOH-FHSIS) or Department of Health- Philippine Integrated
    Disease Surveillance and Response (DOH-PISDR). When adm4_pcode is not available,
    data is in a city level resolution. This data, requested by Epimetrics from their
    respective data owners, is governed by Data Use Agreements that allows for public
    use for climate and health applications.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/1f10c8ee-37a9-40b6-a18a-e8fbe4bb7173/download/disease_lgu_disaggregated_totals.csv
  format: null
  id: resource_1f10c8ee
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disease_lgu_disaggregated_totals.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Long term basic weather parameters related to the atmosphere. For parameters
    extracted from ERA5 , Coordinated Universal Time (UTC) was converted to Philippine
    Time (PHT) by adding 8 hours. The daily values were determined by taking the average
    per day (00:00 PHT - 23:00 PHT). For parameters extracted from CHIRPS (precipitation
    and precipitation-derived indices), it is worth noting that it is a land-only
    datasets and barangays with no available data may not have been represented as
    land in the dataset. Datasets for temperature and precipitation were chosen based
    on an evaluation comparing values with ground truth data from the Philippine Atmospheric,
    Geophysical, and Astronomical Services Administration (PAGASA).
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/8bf5b884-77af-4c38-aeee-3380a4d8e029/download/climate_atmosphere.csv
  format: null
  id: resource_8bf5b884
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: climate_atmosphere.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Output from the Project CCHAIN deep learning climate downscaling model\
    \ . The model yielded improved minimum temperature, maximum temperature and rainfall\
    \ by enhancing its resolution from the reanalysis scale (0.25\xB0) to local scale\
    \ (0.02\xB0). While we provide the full downscaled output as gridded netcdf files\
    \ here for all the 12 cities, only those variables that passed our quality checks\
    \ (QC) are included in this table. Kindly read the documentation before deciding\
    \ to use this data. If you are uncertain, consider using the climate_atmosphere\
    \ table instead"
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/a070a35e-5b75-44de-a1b2-08bc7aa2ff07/download/climate_atmosphere_downscaled.csv
  format: null
  id: resource_a070a35e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: climate_atmosphere_downscaled.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Long term estimates of air quality parameters. For parameters extracted
    from ERA5 , Coordinated Universal Time (UTC) was converted to Philippine Time
    (PHT) by adding 8 hours. The daily values were determined by taking the average
    per day (00:00 PHT - 23:00 PHT). For parameters extracted from CAMS , 3-hourly
    UTC values were converted to PHT by adding 8 hours. As such, there is no value
    for 2003-01-01 and the value for 2003-01-02 is the mean of the available six timesteps.
    Complete data is available for 2003-01-03 onwards. For parameters extracted from
    MERRA-2 , 3-hourly UTC values were converted to PHT by adding 8 hours.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/762426c4-b28a-43be-9fec-1ad564d3c38d/download/climate_air_quality.csv
  format: null
  id: resource_762426c4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: climate_air_quality.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Long term estimates of rainfall-derived parameters. Note that these
    indices were all derived from precipitation values from CHIRPS which is a land-only
    dataset. Barangays with no available data may not have been represented as land.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/b1454765-704c-47ad-ae15-43a4d010f768/download/climate_indices.csv
  format: null
  id: resource_b1454765
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: climate_indices.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Long term estimates of land-related parameters. In the selection of
    an NDVI dataset, MCD19A3CMG was preferred over MCD19A3D due to its provision in
    a geographic latitude and longitude coordinate system and the collection of data
    in one raw file per day.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/07014e15-bdee-4a8e-a0ae-9e58d790432f/download/climate_land.csv
  format: null
  id: resource_07014e15
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: climate_land.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DOES NOT CONTAIN CLIMATE VARIABLES . Log of hourly timesteps used to
    check the aggregates generated by processing raw climate parameters to daily scale,
    extracted from MERRA-2 in climate_air_quality . Use this only as QC layer to climate_air_quality
    This table is to be used in conjunction with climate_air_quality where carbon
    monoxide (CO) and sulfur dioxide (SO2) are extracted from MERRA-2. There is a
    possibility of missing timesteps after conversion to local time and so the number
    of timesteps available daily were extracted to quantify the reliability of data.
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/80d541cb-73d5-4201-b7da-80b77f0c9bd8/download/climate_timestep_check.csv
  format: null
  id: resource_80d541cb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: climate_timestep_check.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DOH Health facilities from the GeoPortal platform . Further definitions
    of each health facility type and descriptions about the data source can be found
    in the linked platform. Processing is similar to how OSM POIs were aggregated.
    Further details can be found in the github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/3ca89d0e-3671-4f63-8dff-9af3e05b93cc/download/geoportal_doh_poi_health.csv
  format: null
  id: resource_3ca89d0e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: geoportal_doh_poi_health.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Select OpenStreetMap (OSM) amenities that include basic public and
    private service facilities for communities. List of all available OSM amenity
    types can be found in their wiki page . Statistics for each POI type (sum and
    nearest distance) was done for every barangay through vector zonal statistics.
    To note, during our investigation it was found that there are not a lot of POIs
    particularly for hospitals and clinics. Making sure that we captured as much data
    as possible we augmented this by also processing OSM buildings and filtering only
    those that related to health and added them to the dataset. Further details on
    the processing of POIs and OSM buildings can be found in the github repository
    .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/fb7040cf-4bbc-49ec-9721-7e13ba3c9530/download/osm_poi_amenity.csv
  format: null
  id: resource_fb7040cf
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osm_poi_amenity.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: OpenStreetMap (OSM) health facilities available for each barangay.
    Listed in the OSM wiki page are the different POIs related to health are available.
    Statistics for each POI type (sum and nearest distance) was calculated for every
    barangay through vector zonal statistics. To note, during our investigation it
    was found that there are not a lot of POIs particularly for hospitals and clinics.
    Making sure that we captured as much data as possible we augmented this by also
    processing OSM buildings and filtering using the building types only those that
    related to health and added them to this dataset. Further details on the processing
    of POIs and OSM buildings can be found in the github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/6d3dab4b-69d6-49f0-8121-67277612041b/download/osm_poi_health.csv
  format: null
  id: resource_6d3dab4b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osm_poi_health.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: OpenStreetMap (OSM) has a category of amenities for water and sanitation
    facilities. List of the available water and sanitation facilities can be found
    in their wiki page along with the description of each POI. Statistics for each
    POI type (sum and nearest distance) was done for every barangay through vector
    zonal statistics. To note, during our investigation it was found that there are
    not a lot of POIs particularly for hospitals and clinics. Making sure that we
    captured as much data as possible we augmented this by also processing OSM buildings
    and filtering only those that related to health and added them to the dataset.
    Further details on the processing of POIs and OSM buildings can be found in the
    github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/eb1341ec-296f-442c-a741-6e78fca31332/download/osm_poi_sanitation.csv
  format: null
  id: resource_eb1341ec
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osm_poi_sanitation.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Using the OpenStreetMap (OSM) water bodies and waterways their nearest
    distance of each barangay was calculated. See definitions in these links for OSM
    water bodies and OSM waterways . Nearest distance for each water/waterway type
    was done for every barangay through vector zonal statistics. Further details on
    the processing of POIs and OSM buildings can be found in the github repository
    .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/8e4b51fc-3b92-4012-b69a-2d23ed454654/download/osm_poi_water_body.csv
  format: null
  id: resource_8e4b51fc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osm_poi_water_body.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Open, validated health, climate, environment and socioeconomic
    data (OpenStreetMap (OSM) total count of Points of Interests (POIs) for each barangay)
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/353dda97-8fb3-41eb-a6e8-93e07c83732e/download/osm_poi_total.csv
  format: null
  id: resource_353dda97
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osm_poi_total.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Land cover area percentages computed from ESA WorldCover rasters. Descriptions
    of each land cover type can be found in their documentation website and the said
    rasters can be downloaded from the same link. To compute for land cover area percentages,
    the raster was converted to a vector and are then spatially joined with the barangay
    AOIs to compute for the total intersected area and their percentage. More details
    can be found in our github repository
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/737c13eb-2266-40b0-b532-1982cef50efe/download/esa_worldcover.csv
  format: null
  id: resource_737c13eb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: esa_worldcover.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Hazard level area percentages for flooding and landslides from Project
    NOAH . For the flood level definitions, it is as follows: low flood hazard level
    is a knee-level flood, a medium flood hazard level is knee to neck level, and
    a high flood hazard level is described as flood that is above the neck. Further
    information on the data source can be found in the download link from their home
    page. More details on the processing of the hazard level area percentages can
    be found in the github repository .'
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/b767e99d-8044-4ebb-a68a-0803a8a15c2b/download/project_noah_hazards.csv
  format: null
  id: resource_b767e99d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: project_noah_hazards.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Built-up area statistics were computed for each barangay based on Google
    Open Buildings v3 . Google Open Buildings file can be downloaded from their website.
    After locally downloading, the dataset was cropped to the target cities and the
    built-up area statistics were then computed. More detailed steps on the processing
    can be found in github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/107da350-6d50-48cd-b001-d5dcdfaafee7/download/google_open_buildings.csv
  format: null
  id: resource_107da350
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: google_open_buildings.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Percent accessible barangay population within a 5-30 minutes travel
    time from nearest health facility based on the Mapbox Isochrones API . For details
    on the use of the API and the processing of the isochrone contours, these can
    be found in the github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/d8b70ecf-d796-4d0e-a028-04c83904e905/download/mapbox_health_facility_brgy_isochrones.csv
  format: null
  id: resource_d8b70ecf
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mapbox_health_facility_brgy_isochrones.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Percent accessible city population within a 5-30 minutes travel time
    from nearest health facility based on the Mapbox Isochrones API . For details
    on the use of the API and the processing of the isochrone contours, these can
    be found in the github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/4f2f636d-d267-4132-9ae0-e407151ca1c4/download/mapbox_health_facility_city_isochrones.csv
  format: null
  id: resource_4f2f636d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mapbox_health_facility_city_isochrones.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded population estimates from WorldPop . WorldPop population count
    and density estimates ranges from years 2000 to 2020. Population count and population
    density rasters are aligned to each barangay using raster zonal statistics to
    compute for the aggregations. More detailed validation and processing steps can
    be found in our github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/53b885f1-c90c-4f79-b618-8af9530366aa/download/worldpop_population.csv
  format: null
  id: resource_53b885f1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: worldpop_population.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Aggregated internet speed measurements from Ookla for mobile and fixed
    devices. Ookla open data is available from 2019-2022. Data is downloaded through
    their API and more detailed steps can be found in the github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/db5cc208-6af5-4d50-be42-0a52ce425db1/download/ookla_internet_speed.csv
  format: null
  id: resource_db5cc208
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ookla_internet_speed.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nighttime irradiance measurements from Payne Institute for Public Policy.
    To download the raw nighttime lights rasters, it can be accessed through the EOG
    portal through direct download or API download. Data is available from years 2012
    to 2021. For extracting average radiance values, made use of only the annual rasters
    for faster and lighter processing. More details on the processing steps can be
    found in our github repository .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/7e5ff9be-6a8b-425b-9a62-b77ae1068b14/download/nighttime_lights.csv
  format: null
  id: resource_7e5ff9be
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nighttime_lights.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Open, validated health, climate, environment and socioeconomic
    data (Wealth index estimates from a machine learning model (reference here ))
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/21b81755-4aa3-4b11-b57b-b55cf63b978c/download/tm_relative_wealth_index.csv
  format: null
  id: resource_21b81755
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tm_relative_wealth_index.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Building outlines and annotations from a sampling of 250x250m tiles
    within chosen cities. These tiles were carefully selected to focus on residential
    areas with diverse neighborhood densities, terrains, and levels of urbanization,
    as well as areas not yet mapped in OpenStreetMap. Each outline was drawn using
    a combination of visual inspection of satellite imagery, local knowledge, and
    validation from household survey data to cover all buildings present in the tile.
    The attributes contain variables designed to indicate potential wealth markers
    useful for vulnerability analysis, and can also be used in computer vision models
    to expand the spatial coverage of the dataset. This table is also released as
    its own, standalone dataset, TM Open Buildings, which can be viewed here . It
    is also hosted separately for download in Kaggle and HDX .
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/eeef7c8c-939e-4ec9-877b-2c06962c5a27/download/tm_open_buildings.csv
  format: null
  id: resource_eeef7c8c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tm_open_buildings.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Open, validated health, climate, environment and socioeconomic
    data (Standard calendar with dates from 2003-01-01 to 2022-12-31)
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/85cbfd03-4094-4d07-9dbc-e982f524caf9/download/calendar.csv
  format: null
  id: resource_85cbfd03
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: calendar.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Open, validated health, climate, environment and socioeconomic
    data (List of included climate and disaster sensitive diseases)
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/0bfe24d0-396a-4906-82ee-202e90d798f8/download/disease.csv
  format: null
  id: resource_0bfe24d0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disease.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Open, validated health, climate, environment and socioeconomic
    data (Administrative level identifier data for chosen cities up to barangay (adm4))
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/31a3dddb-decc-4fd7-a0f7-acff922a7a76/download/location.csv
  format: null
  id: resource_31a3dddb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: location.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Open, validated health, climate, environment and socioeconomic
    data (Barangay level geographical data, area, and distance to coastlines)
  download_url: https://data.humdata.org/dataset/5b580664-365e-4d7e-b5e5-2990df8f12a5/resource/56685f81-2ac5-40c0-922a-84f3f996be5b/download/brgy_geography.csv
  format: null
  id: resource_56685f81
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: brgy_geography.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_tmds_openvalidatedhealthclimat_2003
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-03-31'
  start: '2003-01-01'
temporal_resolution: null
title: Philippines - Open, validated health, climate, environment and socioeconomic
  data
version: null
vulnerability: null
---
