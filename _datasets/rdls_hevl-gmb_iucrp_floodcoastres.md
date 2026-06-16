---
attributions:
- entity:
    affiliation: null
    email: clorillou@worldbank.org
    name: Cecile Lorillou
    url: https://www.worldbank.org
  id: attribution_ttl
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: null
    name: ACP-EU Natural Disaster Risk Reduction Program
    url: https://capacity4dev.europa.eu/groups/drr-acp/info/acp-eu-natural-disaster-risk-reduction-program_en
  id: attribution_funder
  role: funder
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: pchrzanowski@worldbank.org
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  affiliation: null
  email: info@haskoning.com
  name: Royal HaskoningDHV
  url: https://www.haskoning.com/
dataset_id: rdls_hevl-gmb_iucrp_floodcoastres
description: Risk data package for the Greater Banjul Area (GBA), The Gambia, providing
  flood hazard (urban/pluvial maximum water depth and coastal flat water-level scenarios),
  coastal erosion hazard zones, exposure layers (land use, critical facilities, essential
  access routes, study boundaries), and derived risk/loss rasters for baseline and
  future horizons (2020, 2040, 2070).
details: 'Inventory review indicates the package includes: (i) flood hazard GeoTIFFs
  under `02 Flood hazard` for Urban (21 rasters; return period labels T04, T1, T5,
  T10, T25, T100, T250 across horizons current/2040/2070) and Coastal (15 rasters;
  flat scenario water level in meters across 2020/2040/2070 with labels 0.4/1/10/30/100);
  (ii) coastal erosion vectors in `Erosion hazard.gdb` (2040/2070 erosion zones plus
  Jan 2020 reference coastline); (iii) exposure vectors in `Landuse.gdb` (land use
  polygons, critical facilities points/polygons, essential roads) and `Areas.gdb`
  (areas and project boundary); and (iv) downstream outputs in `04 Risk` (9 risk rasters
  for Coastal/Urban/Combined x 2020/2040/2070) and `05 Damage` (33 GeoTIFF rasters,
  with naming patterns indicating max water depth and flat scenario layers; unit/meaning
  should be confirmed to distinguish hazard-depth intermediates from monetary damage
  surfaces).'
exposure:
- asset_type:
    description: Population exposure in the Greater Banjul Area classified using the
      GEM GED4ALL schema, sourced from the IUCRP project surveys.
    id: sei-pop
    scheme: GED4ALL
    title: Population taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: population
  id: exposure_gba_population
  metrics:
  - dimension: population
    id: metric_gba_population_individuals
    measurement:
      quantity_kind: count
      unit: count
  - dimension: population
    id: metric_gba_population_households
    measurement:
      quantity_kind: count
      unit: count
  - dimension: population
    id: metric_gba_population_poor_individuals
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Building stock in the Greater Banjul Area classified using the GEM
      GED4ALL schema.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exposure_gba_buildings
  metrics:
  - dimension: structure
    id: metric_gba_building_count
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Critical facilities and infrastructure in the Greater Banjul Area
      derived from land use mapping (IUCRP project).
    id: critical_facilities
    scheme: null
    title: Infrastructure taxonomy
    uri: null
  category: infrastructure
  id: exposure_gba_critical_facilities_infrastructure
  metrics:
  - dimension: structure
    id: metric_gba_critical_facility_count
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 7
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_flood_urban_pluvial
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_flood_urban_pluvial_occurrence
    occurrence_range: 'Time horizons: current (baseline), 2040, 2070; 7 return-period
      rasters per horizon: T1, T4, T5, T10, T25, T100, T250 (some also provided as
      corrected variants). Per-horizon raster naming: ''T{RP}_max_wd_{horizon}.tif''
      (raw) and ''T{RP}_max_wd_{horizon}_corrected.tif'' (corrected).'
    seasonality: null
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 5
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_flood_coastal
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_flood_coastal_flat_scenario_occurrence
    occurrence_range: 'Time horizons: 2020, 2040, 2070; 5 probability/return-period
      classes encoded in rasters per horizon: 0.4, 1, 10, 30, 100. Per-horizon water-level
      values (m above datum) observed in raster filenames - 2020: {0.4: 2.38, 1: 2.42,
      10: 2.52, 30: 2.57, 100: 2.62}; 2040: {0.4: 2.48, 1: 2.52, 10: 2.62/2.72, 30:
      2.67, 100: 2.72}; 2070: {0.4: 2.70, 1: 2.74, 10: 2.84, 30: 2.89, 100: 2.94}.
      File naming pattern: ''flat scenario_{water_level}m_{year}_{class}.tif''. Some
      filenames contain minor formatting inconsistencies (spaces / double .tif) -
      treat as semantic rather than literal string matching.'
    seasonality: null
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 5
    events:
    - calculation_method: simulated
      description: Reference coastline linework (baseline). Delivered in the coastal
        erosion geodatabase as 'Reference_coastline_2020'. Used as the baseline shoreline
        for defining erosion hazard offsets/zones.
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_erosion
        intensity_measure: Er:m/yr
        process: coastal_erosion
        trigger: null
        type: erosion
      id: event_coastal_erosion_reference_coastline_2020
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: Permanent/structural erosion zone for 2040 horizon, delivered as
        'Erosion_zone_2040_permanent'. Represents irreversible shoreline retreat component
        (e.g., SLR-driven and/or structural erosion trend).
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_erosion
        intensity_measure: Er:m/yr
        process: coastal_erosion
        trigger: null
        type: erosion
      id: event_coastal_erosion_permanent_2040
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: Combined erosion zone for 2040 horizon delivered as 'Erosion_zone_2040_permanent_and_temporary_storm_erosion'.
        This layer represents permanent (structural) erosion plus an additional temporary
        storm erosion buffer.
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_erosion
        intensity_measure: Er:m/yr
        process: coastal_erosion
        trigger: null
        type: erosion
      id: event_coastal_erosion_permanent_plus_temporary_storm_2040
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: Permanent/structural erosion zone for 2070 horizon, delivered as
        'Erosion_zone_2070_permanent'.
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_erosion
        intensity_measure: Er:m/yr
        process: coastal_erosion
        trigger: null
        type: erosion
      id: event_coastal_erosion_permanent_2070
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    - calculation_method: simulated
      description: Combined erosion zone for 2070 horizon delivered as 'Erosion_zone_2070_permanent_and_temporary_storm_erosion'.
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_coastal_erosion
        intensity_measure: Er:m/yr
        process: coastal_erosion
        trigger: null
        type: erosion
      id: event_coastal_erosion_permanent_plus_temporary_storm_2070
      occurrence:
        deterministic:
          description: null
          index_criteria: Scenario-based deterministic analysis
          thresholds: null
        empirical: null
        probabilistic: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_coastal_erosion
      intensity_measure: Er:m/yr
      process: coastal_erosion
      trigger: null
      type: erosion
    id: event_set_coastal_erosion_hazard_zones
    occurrence_range: Erosion hazard lines/zones for baseline reference and future
      horizons (2040, 2070), including permanent (structural/SLR-related) and combined
      permanent+temporary storm erosion representations.
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood and coastal risk assessment for the Greater Banjul Area (GBA),
    The Gambia, produced by Royal HaskoningDHV under the ACP-EU Natural Disaster Risk
    Reduction programme (GFDRR). Fluvial, pluvial, and coastal flood hazard modelled
    using 2D hydrodynamic simulation for 2020, 2040, and 2070 time horizons, incorporating
    IPCC-based sea level rise and rainfall change projections. Coastal erosion zones
    derived from satellite-based shoreline change analysis supplemented by NDMA field
    observations and historical storm records. Land use and critical facility inventory
    compiled from the GBA land use map. Exposure and loss estimates used population
    and poverty density maps projected to 2040 and 2070 using census growth rates.
    Damage computed by applying depth-damage vulnerability functions to spatially
    intersected hazard and exposure layers.
  sources:
  - id: source_1
    license: null
    name: Flood hazard assessment (fluvial, pluvial, coastal) - project hazard modelling
      workflow
    risk_data_type: null
    type: model
    url: https://www.fathom.global/
    used_in: hazard
  - id: source_2
    license: null
    name: Coastal erosion hazard assessment - shoreline change and storm erosion workflow
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: IPCC-based sea level rise and rainfall change projections (used for climate
      change assumptions)
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: NDMA field observations and prior workshop flood observations (validation
      reference)
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: Historical satellite data for shoreline change analysis
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
  - id: source_6
    license: null
    name: Land use map and critical infrastructure layers (Greater Banjul Area)
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_7
    license: null
    name: Population density maps (current/2040/2070) - derived from census and growth
      projections
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_8
    license: null
    name: Poverty rate at national poverty line maps (2040/2070) - derived from census
      and growth projections
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
  - id: source_9
    license: null
    name: Depth-damage functions (damage functions / vulnerability curves)
    risk_data_type: null
    type: model
    url: null
    used_in: exposure
  - id: source_10
    license: null
    name: Economic values (asset/land-use economic valuation inputs)
    risk_data_type: null
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Urban flood loss outputs for Greater Banjul Area derived from probabilistic
      pluvial flood hazard modelling and depth-damage functions applied to building
      / land-use exposure. Inventory indicates urban return-period rasters with naming
      pattern: T{RP}_max_wd_{year}_corrected.tif (e.g., T1/T5/T10/T25/T100/T250 for
      current/2040/2070). Confirm whether values represent monetary losses (USD) or
      intermediate depth grids; treat as economic loss layers per project methodology
      described in the PDFs.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_urban_pluvial_buildings_monetary
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Coastal flood loss outputs for Greater Banjul Area derived from
      coastal inundation ''flat'' sea-level scenarios combined with exposure and depth-damage
      functions. Inventory indicates coastal scenario rasters under 2020/2040/2070
      with naming pattern: flat scenario_{waterlevel}m_{year}_{class}.tif (e.g., 0.4/1/10/30/100
      classes; water levels vary by horizon). Confirm whether stored rasters are monetary
      loss values (USD) or intermediate inundation depths; treat as economic loss
      layers per project methodology described in the PDFs.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_coastal_flat_buildings_monetary
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: development_index
    asset_dimension: index
    description: Risk / prioritization index rasters provided as corrected risk surfaces
      for Coastal, Urban, and Combined cases for 2020/2040/2070 (e.g., Coastal_2020_risk_corrected.tif,
      Urban_2040_risk_corrected.tif, Combined_2070_risk_corrected.tif). Interpreted
      as a normalized damage/risk index (non-monetary). If these rasters actually
      represent expected annual loss (EAL/AAL) or other monetary risk metrics, re-map
      impact_metric to loss_annual_average_value and set quantity_kind=monetary with
      currency=USD.
    disaster_identifiers: []
    hazard:
      classification: null
      id: null
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_risk_index_corrected
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage_index
        modelling: simulated
        type: direct
      loss_approach: hybrid
      loss_frequency_type: probabilistic
      loss_type: gross
project:
  name: The Gambia Integrated Urban and Coastal Resilience Program
  url: https://www.gfdrr.org/en/gambia-integrated-urban-and-coastal-resilience-technical-assistance-program
publisher:
  affiliation: null
  email: data@gfdrr.org
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support flood and coastal risk assessment and the prioritization of investment
  options for resilience in the Greater Banjul Area by providing spatial hazard, exposure,
  and risk/loss datasets for current conditions and future horizons.
referenced_by: []
resources:
- access_url: https://geowb.maps.arcgis.com/apps/MapJournal/index.html?appid=a7884f06912c4e73a73c49a9feebda68#
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: ArcGIS Map Journal web application providing an interactive narrative
    overview of the flood and coastal risk assessment for the Greater Banjul Area.
    Presents key findings, hazard maps, risk outputs, and investment planning recommendations
    through an interactive dashboard interface.
  download_url: null
  format: Web application
  id: resource_storymap
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Interactive Story Map - Flood and Coastal Risk Assessment for Greater Banjul
- access_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32628
  description: 'Zip archive containing vector exposure data for the Greater Banjul
    Area. Includes the File Geodatabase Landuse.gdb with four key layers: (1) LU_GBA_5_0
    - land use polygons with attribute Category (e.g., Residential, Shrubs, Forest,
    essential access routes); (2) Road_essential - lines with attribute eclass (e.g.,
    Essential access routes paved/unpaved); (3) Critical_facilities - polygons with
    building_name and Category (e.g., Hospital, School, Fire Station); (4) Critical_facilities_point
    - points with Category_2 and name_building. Also includes LU_GBA_5_0.zip packaging
    the land use polygon layer as a Shapefile set for GIS interoperability.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095906/01_Landuse.zip
  format: null
  id: resource_landuse
  media_type: application/x-filegdb
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Land Use and Exposure Layers
- access_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32628
  description: 'Zip archive containing 36 flood hazard GeoTIFF rasters for the Greater
    Banjul Area, organized into Coastal and Urban subfolders for time horizons 2020,
    2040, and 2070. Urban flood hazard (21 files): maximum water depth rasters following
    naming convention T{RP}_max_wd_{YEAR}.tif, where RP indicates return period category
    (T04, T1, T5, T10, T25, T100, T250) for each horizon (current/2020, 2040, 2070).
    Coastal flood hazard (15 files): flat scenario inundation rasters following naming
    convention flat scenario_{water_level}m_{YEAR}_{RP}.tif, where water_level is
    the total water level in meters and RP is the return period class (0.4, 1, 10,
    30, 100 years) for each horizon. Intensity measure: maximum water depth in meters.
    Coordinate system: WGS84 / UTM zone 28N (EPSG:32628).'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095907/02_Flood_Hazard.zip
  format: null
  id: resource_flood_hazard
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flood Hazard Rasters - Coastal and Urban
- access_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32628
  description: 'Zip archive containing an Esri File Geodatabase (Erosion hazard.gdb)
    with coastal erosion hazard vector layers for the Greater Banjul Area. Contains
    5 line feature layers: (1) Erosion_zone_2040_years_Permanent_erosion - permanent
    erosion zone projected to 2040; (2) Erosion_zone_2040_years_Permanent_erosion_Temporary_storm_erosion
    - combined permanent and temporary storm erosion zone for 2040; (3) Erosion_zone_2070_permanent
    - permanent erosion zone projected to 2070; (4) Erosion_zone_2070_years_Permanent_erosion_Temporary_storm_erosion
    - combined permanent and temporary storm erosion zone for 2070; (5) Reference_coastline_position_January_2020
    - baseline reference coastline.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095908/03_Erosion_Hazard.zip
  format: null
  id: resource_erosion_hazard
  media_type: application/x-filegdb
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal Erosion Hazard Vectors
- access_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32628
  description: Zip archive containing 9 risk output GeoTIFF rasters for the Greater
    Banjul Area, providing three risk surfaces (Coastal, Urban, Combined) for each
    time horizon 2020, 2040, and 2070. Files follow the naming convention {TYPE}_{YEAR}_risk_corrected.tif
    where TYPE is Coastal, Urban, or Combined. These are downstream products derived
    from the hazard-exposure-vulnerability workflow, integrating flood hazard depth
    with land use exposure and damage functions to produce spatially distributed risk
    estimates.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095909/04_Risk.zip
  format: null
  id: resource_risk
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Risk Output Rasters - Coastal, Urban, and Combined
- access_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32628
  description: Zip archive containing 33 GeoTIFF rasters for the Greater Banjul Area,
    organized by Coastal and Urban subfolders for time horizons 2020, 2040, and 2070.
    Urban rasters (stored under Urban {YEAR} folders) follow naming convention T{RP}_max_wd_{YEAR}_corrected.tif,
    representing corrected maximum water depth surfaces per return period. Coastal
    rasters (stored under Coastal {YEAR} uncorrected folders) follow naming convention
    flat scenario_{water_level}m_{YEAR}_{RP}.tif, representing coastal inundation
    depth surfaces. These rasters serve as intermediate depth outputs used in conjunction
    with exposure and vulnerability data to compute the risk_corrected rasters in
    the Risk package.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095910/05_Damage.zip
  format: null
  id: resource_damage
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Damage Rasters - Coastal and Urban Flood Depth Outputs
- access_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32628
  description: 'Zip archive containing an Esri File Geodatabase (Areas.gdb) with supporting
    polygon boundaries for the Greater Banjul Area study. Contains two polygon layers:
    (1) Areas - study/aggregation units used for hotspot reporting and summarization
    of risk results across the Greater Banjul Area (Banjul, Kanifing Municipality,
    Kombo North/Central/South); (2) Project_boundary - overall project boundary/extent
    delineating the geographic scope of the flood and coastal risk assessment.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066938/DR0095911/06_Areas.zip
  format: null
  id: resource_areas
  media_type: application/x-filegdb
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Project Boundary and Study Areas
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdls-10
slug: rdls_hevl-gmb_iucrp_floodcoastres
spatial:
  bbox: null
  centroid: null
  countries:
  - GMB
  gazetteer_entries:
  - description: Banjul
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/2413876/banjul.html
  - description: Kanifing
    id: gazetteer_2
    scheme: GEONAMES
    uri: https://www.geonames.org/2413106/kanifing.html
  scale: sub-national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2070'
  start: '2020'
temporal_resolution: null
title: Flood and Coastal Risk Assessment and Priority Investment Planning for Greater
  Banjul Area, The Gambia
version: '1'
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility: []
    socio_economic: []
    vulnerability:
    - analysis_details: Depth-damage vulnerability functions used to convert flood
        inundation water depth (wd:m) into a damage ratio by asset / land-use class
        (e.g., residential, commercial/industrial, critical facilities) for the Greater
        Banjul Area urban flood risk assessment. Applied together with exposure layers
        (land use, critical facilities) and per-unit economic values (where available
        in project materials) to estimate direct economic flood damages and derived
        risk outputs.
      approach: hybrid
      category: buildings
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: wd:m
        process: pluvial_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vulnerability_function_1
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: Custom
    - analysis_details: Depth-damage vulnerability functions used to convert coastal
        inundation water depth (wd:m) into a damage ratio by asset / land-use class
        for the Greater Banjul Area coastal flood risk assessment (including sea level
        rise 'flat' scenarios and related coastal inundation outputs). Applied together
        with exposure layers (land use, critical facilities) and per-unit economic
        values (where available in project materials) to estimate direct economic
        coastal flood damages and derived risk outputs.
      approach: hybrid
      category: buildings
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: null
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      hazard_secondary: null
      id: vulnerability_function_2
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: damage
        modelling: simulated
        type: direct
      relationship: discrete
      taxonomy: Custom
---
