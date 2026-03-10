---
catalog: World Bank Data Catalog
contact_point:
  email: pchrzanowski@worldbank.org
  id: attribution_contact
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  email: info@haskoning.com
  id: attribution_creator
  name: Royal HaskoningDHV
  url: https://www.haskoning.com/
dataset_id: rdls_lss-gmb_floodcoastres
description: Risk data package for the Greater Banjul Area (GBA), The Gambia, providing
  flood hazard (urban/pluvial maximum water depth and coastal flat water-level scenarios),
  coastal erosion hazard zones, exposure layers (land use, critical facilities, essential
  access routes, study boundaries), and derived risk/loss rasters for baseline and
  future horizons (2020, 2040, 2070).
details: "Inventory review indicates the package includes: (i) flood hazard GeoTIFFs\
  \ under `02 Flood hazard` for Urban (21 rasters; return period labels T04, T1, T5,\
  \ T10, T25, T100, T250 across horizons current/2040/2070) and Coastal (15 rasters;\
  \ flat scenario water level in meters across 2020/2040/2070 with labels 0.4/1/10/30/100);\
  \ (ii) coastal erosion vectors in `Erosion hazard.gdb` (2040/2070 erosion zones\
  \ plus Jan 2020 reference coastline); (iii) exposure vectors in `Landuse.gdb` (land\
  \ use polygons, critical facilities points/polygons, essential roads) and `Areas.gdb`\
  \ (areas and project boundary); and (iv) downstream outputs in `04 Risk` (9 risk\
  \ rasters for Coastal/Urban/Combined \xD7 2020/2040/2070) and `05 Damage` (33 GeoTIFF\
  \ rasters, with naming patterns indicating max water depth and flat scenario layers;\
  \ unit/meaning should be confirmed to distinguish hazard-depth intermediates from\
  \ monetary damage surfaces)."
exposure:
- category: population
  dimension: population
  quantity_kind: count
  taxonomy: GED4ALL
- category: buildings
  dimension: structure
  quantity_kind: count
  taxonomy: GED4ALL
- category: infrastructure
  dimension: structure
  quantity_kind: count
  taxonomy: GED4ALL
extra_attributions:
- email: clorillou@worldbank.org
  id: attribution_ttl
  name: Cecile Lorillou
  role: world_bank_team_lead
  url: https://www.worldbank.org
- email: https://capacity4dev.europa.eu/contact_en
  id: attribution_funder
  name: ACP-EU Natural Disaster Risk Reduction Program
  role: funder
  url: https://capacity4dev.europa.eu/groups/drr-acp/info/acp-eu-natural-disaster-risk-reduction-program_en
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: deterministic, probabilistic
  hazard_type: coastal_flood, flood, landslide
  intensity: wd:m
  occurrence_range: 'Erosion hazard lines/zones for baseline reference and future
    horizons (2040, 2070), including permanent (structural/SLR-related) and combined
    permanent+temporary storm erosion representations., Time horizons: 2020, 2040,
    2070; probability/return-period classes encoded in rasters: 0.4, 1, 10, 30, 100
    (as in filenames)., Time horizons: current (baseline), 2040, 2070; return periods
    encoded in rasters: T1, T4, T5, T10, T25, T100, T250 (some also provided as corrected
    variants).'
  processes: coastal_flood, landslide_general, pluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: "Coastal flood loss outputs for Greater Banjul Area derived from coastal\
    \ inundation \u2018flat\u2019 sea-level scenarios combined with exposure and depth-damage\
    \ functions. Inventory indicates coastal scenario rasters under 2020/2040/2070\
    \ with naming pattern: flat scenario_{waterlevel}m_{year}_{class}.tif (e.g., 0.4/1/10/30/100\
    \ classes; water levels vary by horizon). Confirm whether stored rasters are monetary\
    \ loss values (USD) or intermediate inundation depths; treat as economic loss\
    \ layers per project methodology described in the PDFs., Risk / prioritization\
    \ index rasters provided as corrected risk surfaces for Coastal, Urban, and Combined\
    \ cases for 2020/2040/2070 (e.g., Coastal_2020_risk_corrected.tif, Urban_2040_risk_corrected.tif,\
    \ Combined_2070_risk_corrected.tif). Interpreted as a normalized damage/risk index\
    \ (non-monetary). If these rasters actually represent expected annual loss (EAL/AAL)\
    \ or other monetary risk metrics, re-map impact_metric to loss_annual_average_value\
    \ and set quantity_kind=monetary with currency=USD., Urban flood loss outputs\
    \ for Greater Banjul Area derived from probabilistic pluvial flood hazard modelling\
    \ and depth-damage functions applied to building / land-use exposure. Inventory\
    \ indicates urban return-period rasters with naming pattern: T{RP}_max_wd_{year}_corrected.tif\
    \ (e.g., T1/T5/T10/T25/T100/T250 for current/2040/2070). Confirm whether values\
    \ represent monetary losses (USD) or intermediate depth grids; treat as economic\
    \ loss layers per project methodology described in the PDFs."
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: coastal_flood, pluvial_flood
  hazard_type: coastal_flood, flood
  impact_metric: ''
  impact_type: ''
  impact_unit: ''
  type: ''
  vulnerability_id: ''
project:
  name: The Gambia Integrated Urban and Coastal Resilience Program
  url: https://www.gfdrr.org/en/gambia-integrated-urban-and-coastal-resilience-technical-assistance-program
publisher:
  email: data@gfdrr.org
  id: attribution_publisher
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support flood and coastal risk assessment and the prioritization of investment
  options for resilience in the Greater Banjul Area by providing spatial hazard, exposure,
  and risk/loss datasets for current conditions and future horizons.
resources:
- coordinate_system: EPSG:32628
  description: 'Vector exposure package for the Greater Banjul Area. The File Geodatabase
    `Landuse.gdb` contains four key layers: (i) `LU_GBA_5_0` polygons with attribute
    `Category` (e.g., Residential, Shrubs, Forest, and classes representing essential
    access routes); (ii) `Road_essential` lines with attribute `eclass` (e.g., Essential
    access routes paved / unpaved); (iii) `Critical_facilities` polygons with `building_name`
    and `Category` (e.g., Hospital, School, Fire Station); and (iv) `Critical_facilities_point`
    points with `Category_2` and `name_building`. The inventory also includes `LU_GBA_5_0.zip`,
    which packages the land use polygon layer as a Shapefile set.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  format: File Geodatabase (gdb)
  id: resource_1
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Land use and exposure layers (Landuse.gdb + LU_GBA_5_0.zip)
- coordinate_system: EPSG:32628
  description: Flood hazard GeoTIFF rasters under `02 Flood hazard`, organized into
    Coastal and Urban subfolders and provided for horizons 2020, 2040, and 2070. Coastal
    flood hazard rasters (15 files) follow the naming convention `flat scenario_<LEVEL>m_<YEAR>_<LABEL>.tif`,
    where `<LEVEL>` is a water level parameter in meters and `<LABEL>` is an occurrence
    label (commonly 0.4, 1, 10, 30, 100; interpretation as return period/probability
    should be confirmed). Urban flood hazard rasters (21 files) follow the naming
    convention `T<RPLABEL>_max_wd_<YEAR>.tif`, where `max_wd` indicates maximum water
    depth and `T<RPLABEL>` indicates event likelihood label / return period category
    (T04, T1, T5, T10, T25, T100, T250), repeated for each horizon (`current`/2020,
    2040, 2070).
  download_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  format: GeoTIFF (tif)
  id: resource_2
  media_type: null
  spatial_resolution: 5
  temporal: null
  title: Flood hazard rasters (coastal flat scenario + urban maximum water depth)
- coordinate_system: EPSG:32628
  description: 'Coastal erosion hazard vector layers provided as an Esri File Geodatabase
    (`Erosion hazard.gdb`). The geodatabase contains erosion zone line layers for
    horizons 2040 and 2070, distinguishing permanent erosion and permanent+temporary
    storm erosion variants, plus a baseline reference coastline line layer (`Reference_coastline_position_January_2020`).
    Layer names include: `Erosion_zone_2040_years_Permanent_erosion`, `Erosion_zone_2040_years_Permanent_erosion_Temporary_storm_erosion`,
    `Erosion_zone_2070_permanent`, `Erosion_zone_2070_years_Permanent_erosion_Temporary_storm_erosion`,
    and `Reference_coastline_position_January_2020`.'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  format: File Geodatabase (gdb)
  id: resource_3
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Coastal erosion hazard vectors (Erosion hazard.gdb)
- coordinate_system: EPSG:32628
  description: "Risk output GeoTIFF rasters under `04 Risk` providing three risk surfaces\
    \ (Coastal, Urban, Combined) for each horizon year 2020, 2040, and 2070. Files\
    \ follow the naming convention `<TYPE>_<YEAR>_risk_corrected.tif` where `<TYPE>`\
    \ is `Coastal`, `Urban`, or `Combined`. These are downstream products derived\
    \ from the project\u2019s hazard and exposure workflow; the exact metric/unit\
    \ represented by \u201Crisk_corrected\u201D should be confirmed (e.g., risk index\
    \ vs expected annual damage)."
  download_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  format: GeoTIFF (tif)
  id: resource_4
  media_type: null
  spatial_resolution: 5
  temporal: null
  title: Risk outputs (risk_corrected rasters for coastal, urban, and combined)
- coordinate_system: EPSG:32628
  description: "GeoTIFF rasters under `05 Damage`, organized by Coastal and Urban\
    \ subfolders and horizons 2020, 2040, and 2070. Coastal rasters are stored under\
    \ folders labeled `Coastal <YEAR> uncorrected` and use the naming convention `flat\
    \ scenario_<LEVEL>m_<YEAR>_<LABEL>.tif`. Urban rasters are stored under folders\
    \ labeled `Urban <YEAR>` and include files named `T<RPLABEL>_max_wd_<YEAR>_corrected.tif`.\
    \ Although stored in a folder named \u201CDamage\u201D, the naming conventions\
    \ suggest many rasters represent maximum water depth surfaces (hazard intensity);\
    \ confirmation is needed on whether raster values are monetary damage/loss, or\
    \ hazard-depth intermediates used in subsequent loss calculations."
  download_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  format: GeoTIFF (tif)
  id: resource_5
  media_type: null
  spatial_resolution: 5
  temporal: null
  title: Damage folder rasters (05 Damage; coastal flat scenario + urban max_wd corrected)
- coordinate_system: EPSG:32628
  description: 'Supporting polygon boundaries provided as an Esri File Geodatabase
    (`Areas.gdb`). Contains two polygon layers: `Areas` (study/aggregation units used
    for hotspot reporting and summarization) and `Project_boundary` (overall project
    boundary/extent).'
  download_url: https://datacatalog.worldbank.org/search/dataset/0066938/flood_and_coastal_risk_assessment_and_priority_investment_planning_for_greater_banjul_the_gambia
  format: File Geodatabase (gdb)
  id: resource_6
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Project boundary and study areas (Areas.gdb)
risk_data_type:
- hazard
- exposure
- vulnerability
- loss
schema: rdl-03
slug: rdls_lss-gmb_floodcoastres
spatial:
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
title: Flood and Coastal Risk Assessment and Priority Investment Planning for Greater
  Banjul Area, The Gambia
version: '1'
vulnerability:
  approach: hybrid
  base_data_type: simulated
  category: buildings
  dimension: ''
  function_type: ''
  hazard_analysis_type: probabilistic
  hazard_primary: coastal_flood, flood
  hazard_process_primary: coastal_flood, pluvial_flood
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: damage_ratio
  relationship: discrete
  taxonomy: Custom
  unit: ''
---
